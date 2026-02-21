# app/repository.py

"""
Repository abstractions for the Phone Book application.
"""

from abc import ABC, abstractmethod
from app.models import Contact


class ContactRepository(ABC):
    """
    Abstract repository interface for managing contacts.
    """

    @abstractmethod
    def get_all(self) -> list[Contact]:
        """Return all contacts."""
        pass

    @abstractmethod
    def save_all(self, contacts: list[Contact]) -> None:
        """Persist all contacts."""
        pass
