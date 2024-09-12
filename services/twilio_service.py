# services/twilio_service.py

import os
from twilio.rest import Client
from dotenv import load_dotenv

class TwilioService:
    def __init__(self):
        load_dotenv()
        self.client: Client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
        self.from_number: str = 'whatsapp:' + os.getenv("TWILIO_WHATSAPP_NUMBER")

    def send_whatsapp_message(self, to_number: str, message: str) -> None:
        try:
            sent_message = self.client.messages.create(
                body=message,
                from_=self.from_number,
                to='whatsapp:' + to_number
            )
            print(f"Message sent to {to_number} with SID: {sent_message.sid}")
        except Exception as e:
            print(f"Failed to send message to {to_number}: {str(e)}")
