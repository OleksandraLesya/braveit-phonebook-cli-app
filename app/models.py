# app/models.py
"""
Моделі даних для Phone Book CLI.
"""

from uuid import uuid4
from datetime import datetime, UTC


class Contact:
    """
    Клас, що представляє контакт телефонної книги.
    """

    def __init__(
        self,
        first_name: str,
        last_name: str,
        phones: dict,
        city: str = "",
        job: str = "",
        contact_id: str | None = None,
        created_at: str | None = None,
    ):
        self.id = contact_id or str(uuid4())
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.phones = phones
        self.city = city.capitalize() if city else ""
        self.job = job.capitalize() if job else ""
        self.created_at = created_at or datetime.now(UTC).isoformat()

    def to_dict(self) -> dict:
        """Перетворює Contact у словник (для JSON / CSV)."""
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phones": self.phones,
            "city": self.city,
            "job": self.job,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Contact":
        """Створює Contact зі словника."""
        return cls(
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", ""),
            phones=data.get("phones", {}),
            city=data.get("city", ""),
            job=data.get("job", ""),
            contact_id=data.get("id"),
            created_at=data.get("created_at"),
        )
