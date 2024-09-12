import os
from dotenv import load_dotenv

load_dotenv()

def get_personalized_message(nickname: str) -> str:
    """
    Retourne un message personnalisé en utilisant une variable d'environnement.

    :param nickname: Surnom de la personne à insérer dans le message.
    :return: Message personnalisé.
    """
    message_template: str = os.getenv("SECRET_MESSAGE_TEMPLATE", "Hello {nickname}, just a reminder about your important day tomorrow. Stay awesome!")
    return message_template.format(nickname=nickname)
