from dotenv import load_dotenv

from services.reminder_service import ReminderService

def main() -> None:
    load_dotenv()
    reminder_service: ReminderService = ReminderService()
    reminder_service.schedule_reminders()


if __name__ == "__main__":
    main()
