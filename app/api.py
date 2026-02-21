# app/api.py (Dependency Injection)

"""
Business logic layer for the Phone Book application.
"""

from difflib import get_close_matches
from app.models import Contact
from app.repository import ContactRepository
from app.logger import logger


class PhoneBook:
    """
    Core business logic for managing contacts.
    """

    def __init__(self, repository: ContactRepository):
        """
        Initialize PhoneBook with injected repository.
        """
        self.repository = repository
        self.contacts = repository.get_all()

    def _commit(self):
        """Persist current state to repository."""
        self.repository.save_all(self.contacts)

    def add_contact(self, contact: Contact) -> bool:
        if any(c.id == contact.id for c in self.contacts):
            logger.warning("Contact with this ID already exists.")
            return False

        self.contacts.append(contact)
        self._commit()
        return True

    def find_by_id(self, contact_id: str) -> Contact | None:
        return next((c for c in self.contacts if c.id == contact_id), None)

    def delete_contact(self, contact_id: str) -> bool:
        contact = self.find_by_id(contact_id)
        if not contact:
            return False

        self.contacts.remove(contact)
        self._commit()
        return True

    def update_contact(self, contact_id: str, updates: dict) -> bool:
        contact = self.find_by_id(contact_id)
        if not contact:
            return False

        for key, value in updates.items():
            if hasattr(contact, key):
                setattr(contact, key, value)

        self._commit()
        return True

    def search_by_lastname(self, query: str) -> list[Contact]:
        lastnames = [c.last_name for c in self.contacts]
        matches = get_close_matches(query.capitalize(), lastnames, cutoff=0.6)
        return [c for c in self.contacts if c.last_name in matches]

    def search_by_phone(self, query: str) -> list[Contact]:
        return [
            c for c in self.contacts
            if any(query in str(p) for p in c.phones.values())
        ]
