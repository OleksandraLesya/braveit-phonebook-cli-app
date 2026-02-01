# tests/test_models.py

from app.models import create_contact


def test_create_contact_basic_fields():
    contact = create_contact(
        first_name="lesya",
        last_name="ukrainka",
        phones={"mobile": "123456789"},
        city="kyiv",
        job="Python developer",
    )

    assert "id" in contact
    assert contact["first_name"] == "Lesya"
    assert contact["last_name"] == "Ukrainka"
    assert contact["phones"]["mobile"] == "123456789"
    assert contact["city"] == "Kyiv"
    assert contact["job"] == "Python developer"
    assert "created_at" in contact


def test_create_contact_generates_unique_id():
    c1 = create_contact("A", "B", {"mobile": "11111"})
    c2 = create_contact("A", "B", {"mobile": "22222"})

    assert c1["id"] != c2["id"]
