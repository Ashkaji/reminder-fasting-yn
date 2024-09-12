"""
File for loading the contacts
"""
import csv
from operator import delitem
from typing import List, Dict

class CSVLoader:
    @staticmethod
    def load_contacts(file_path: str = 'data/contacts.csv') -> List[Dict[str, str]]:
        """
        Charge les contacts à partir d'un fichier CSV et les trie par 'reminder_day'.

        :param file_path: Chemin vers le fichier CSV des contacts.
        :return: Liste de dictionnaires contenant les informations des contacts, triés par 'reminder_day'.
        """
        contacts: List[Dict[str, str]] = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)

        # Trier les contacts par 'reminder_day'
        contacts.sort(key=lambda x: int(x['reminder_day']))
        return contacts
