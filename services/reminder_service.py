from datetime import datetime, timedelta
from bisect import bisect_left, bisect_right
from typing import List, Dict
from services.twilio_service import TwilioService
from utils.csv_loader import CSVLoader
from utils.message_template import get_personalized_message


class ReminderService:
    def __init__(self):
        self.twilio_service: TwilioService = TwilioService()
        self.contacts: List[Dict[str, str]] = CSVLoader.load_contacts()

    def schedule_reminders(self) -> None:
        today: datetime = datetime.now()
        tomorrow: datetime = today + timedelta(days=1)
        tomorrow_day: int = tomorrow.day

        start_index: int = bisect_left(self.contacts, tomorrow_day, key=lambda x: int(x['reminder_day']))
        end_index: int = bisect_right(self.contacts, tomorrow_day, key=lambda x: int(x['reminder_day']))

        contacts_to_remind: List[Dict[str, str]] = self.contacts[start_index:end_index]

        for contact in contacts_to_remind:
            self.send_reminder(contact)

    def send_reminder(self, contact: Dict[str, str]) -> None:
        nickname: str = contact['nickname']

        if contact['whatsapp_number']:
            number: str = contact['whatsapp_number']
            reminder_message: str = get_personalized_message(nickname)
            self.twilio_service.send_whatsapp_message(number, reminder_message)
