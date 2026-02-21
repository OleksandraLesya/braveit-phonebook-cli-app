"""
Persistence layer for saving and loading contacts using JSON.
Provides automated backup functionality before data modifications.
"""

import json
import os
import shutil
from datetime import datetime
from app.models import Contact
from app.repository import ContactRepository


class JSONStorage(ContactRepository):
    """
    JSON-based implementation of ContactRepository with automated safety backups.
    """

    def __init__(self, filepath: str):
        """
        Initialize storage with a specific file path.
        
        Args:
            filepath (str): Path to the JSON storage file.
        """
        self.filepath = filepath

    def _create_backup(self) -> None:
        """
        Creates a timestamped backup of the current data file if it exists and is not empty.
        Example: phonebook.json -> phonebook.json.20260221_153000.bak
        """
        if os.path.exists(self.filepath) and os.path.getsize(self.filepath) > 0:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = f"{self.filepath}.{timestamp}.bak"
            shutil.copy2(self.filepath, backup_path)

    def get_all(self) -> list[Contact]:
        """
        Load all contacts from the JSON file.
        
        Returns:
            list[Contact]: A list of Contact objects or an empty list if file error occurs.
        """
        if not os.path.exists(self.filepath):
            return []

        try:
            if os.path.getsize(self.filepath) == 0:
                return []

            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Contact.from_dict(item) for item in data]

        except (json.JSONDecodeError, OSError):
            return []

    def save_all(self, contacts: list[Contact]) -> None:
        """
        Persist contacts to a JSON file. 
        Creates a backup before saving, provided the contact list is not empty.
        
        Args:
            contacts (list[Contact]): The list of contacts to save.
        """
        if contacts:
            self._create_backup()

        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(
                [c.to_dict() for c in contacts],
                f,
                ensure_ascii=False,
                indent=2,
            )