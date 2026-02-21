# tests/test_api.py

from app.api import PhoneBook
from app.models import Contact
from app.repository import ContactRepository


class FakeRepository(ContactRepository):
    """
    In-memory fake repository for testing.
    """

    def __init__(self, initial_contacts=None):
        self._contacts = initial_contacts or []

    def get_all(self):
        return list(self._contacts)

    def save_all(self, contacts):
        self._contacts = list(contacts)


def sample_contact(contact_id="1"):
    return Contact(
        first_name="Lesya",
        last_name="Ukrainka",
        phones={"mobile": "12345"},
        city="Kyiv",
        job="QA",
        contact_id=contact_id,
    )


def test_add_contact_success():
    repo = FakeRepository()
    phonebook = PhoneBook(repo)

    contact = sample_contact()
    result = phonebook.add_contact(contact)

    assert result is True
    assert len(phonebook.contacts) == 1


def test_add_contact_duplicate_id():
    contact = sample_contact()
    repo = FakeRepository([contact])
    phonebook = PhoneBook(repo)

    result = phonebook.add_contact(contact)

    assert result is False
    assert len(phonebook.contacts) == 1


def test_delete_contact_success():
    contact = sample_contact("1")
    repo = FakeRepository([contact])
    phonebook = PhoneBook(repo)

    result = phonebook.delete_contact("1")

    assert result is True
    assert phonebook.contacts == []


def test_delete_contact_not_found():
    repo = FakeRepository([sample_contact("1")])
    phonebook = PhoneBook(repo)

    result = phonebook.delete_contact("999")

    assert result is False


def test_update_contact_success():
    contact = sample_contact("1")
    repo = FakeRepository([contact])
    phonebook = PhoneBook(repo)

    result = phonebook.update_contact("1", {"city": "Lviv"})

    assert result is True
    assert contact.city == "Lviv"


def test_update_contact_not_found():
    repo = FakeRepository([sample_contact("1")])
    phonebook = PhoneBook(repo)

    result = phonebook.update_contact("999", {"city": "Odesa"})

    assert result is False


def test_search_by_lastname_fuzzy():
    c1 = sample_contact("1")
    c2 = Contact("Ivan", "Franko", {"mobile": "999"}, contact_id="2")

    repo = FakeRepository([c1, c2])
    phonebook = PhoneBook(repo)

    results = phonebook.search_by_lastname("ukrain")

    assert len(results) == 1
    assert results[0].last_name == "Ukrainka"


def test_search_by_phone_partial():
    c1 = sample_contact("1")
    c2 = Contact("Ivan", "Franko", {"mobile": "987654"}, contact_id="2")

    repo = FakeRepository([c1, c2])
    phonebook = PhoneBook(repo)

    results = phonebook.search_by_phone("876")

    assert len(results) == 1
    assert results[0].phones["mobile"] == "987654"
