# tests/test_api.py

from app.api import (
    add_contact,
    delete_contact,
    update_contact,
    search_by_lastname,
    search_by_phone,
)


def sample_contact(contact_id="1"):
    return {
        "id": contact_id,
        "first_name": "Lesya",
        "last_name": "Ukrainka",
        "phones": {"mobile": "12345"},
        "city": "Kyiv",
        "job": "QA",
    }


def test_add_contact_success():
    phonebook = []
    contact = sample_contact()

    result = add_contact(phonebook, contact)

    assert result is True
    assert len(phonebook) == 1


def test_add_contact_duplicate_id():
    contact = sample_contact()
    phonebook = [contact.copy()]

    result = add_contact(phonebook, contact)

    assert result is False
    assert len(phonebook) == 1


def test_delete_contact_success():
    phonebook = [sample_contact("1")]

    result = delete_contact(phonebook, "1")

    assert result is True
    assert phonebook == []


def test_delete_contact_not_found():
    phonebook = [sample_contact("1")]

    result = delete_contact(phonebook, "999")

    assert result is False


def test_update_contact_success():
    phonebook = [sample_contact("1")]

    result = update_contact(phonebook, "1", {"city": "Lviv"})

    assert result is True
    assert phonebook[0]["city"] == "Lviv"


def test_update_contact_not_found():
    phonebook = [sample_contact("1")]

    result = update_contact(phonebook, "999", {"city": "Odesa"})

    assert result is False


def test_search_by_lastname_fuzzy():
    phonebook = [
        sample_contact("1"),
        {
            "id": "2",
            "first_name": "Ivan",
            "last_name": "Franko",
            "phones": {"mobile": "999"},
        },
    ]

    results = search_by_lastname(phonebook, "ukrain")

    assert len(results) == 1
    assert results[0]["last_name"] == "Ukrainka"


def test_search_by_phone_partial():
    phonebook = [
        sample_contact("1"),
        {
            "id": "2",
            "phones": {"mobile": "987654"},
        },
    ]

    results = search_by_phone(phonebook, "876")

    assert len(results) == 1
    assert results[0]["phones"]["mobile"] == "987654"
