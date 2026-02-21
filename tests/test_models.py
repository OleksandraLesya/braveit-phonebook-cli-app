# tests/test_models.py

from app.models import Contact


def test_contact_basic_fields():
    contact = Contact(
        first_name="lesya",
        last_name="ukrainka",
        phones={"mobile": "123456789"},
        city="kyiv",
        job="Python developer",
    )

    assert contact.id is not None
    assert contact.first_name == "Lesya"
    assert contact.last_name == "Ukrainka"
    assert contact.phones["mobile"] == "123456789"
    assert contact.city == "Kyiv"
    assert contact.job == "Python developer"
    assert contact.created_at is not None


def test_contact_generates_unique_id():
    c1 = Contact("A", "B", {"mobile": "11111"})
    c2 = Contact("A", "B", {"mobile": "22222"})

    assert c1.id != c2.id


def test_contact_to_dict():
    contact = Contact(
        first_name="Test",
        last_name="User",
        phones={"mobile": "999"},
        city="Lviv",
        job="QA",
    )

    data = contact.to_dict()

    assert isinstance(data, dict)
    assert data["first_name"] == "Test"
    assert data["phones"]["mobile"] == "999"


def test_contact_from_dict():
    data = {
        "id": "123",
        "first_name": "Anna",
        "last_name": "Franko",
        "phones": {"mobile": "555"},
        "city": "Odessa",
        "job": "Manager",
        "created_at": "2024-01-01T00:00:00",
    }

    contact = Contact.from_dict(data)

    assert contact.id == "123"
    assert contact.first_name == "Anna"
    assert contact.last_name == "Franko"
    assert contact.phones["mobile"] == "555"
