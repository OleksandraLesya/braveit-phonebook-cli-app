# tests/test_storage.py

import os
from app.storage import JSONStorage
from app.models import Contact

TEST_FILE = "data/test_phonebook.json"


def teardown_function():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_get_all_file_not_exists():
    storage = JSONStorage("data/no_such_file.json")
    result = storage.get_all()
    assert result == []


def test_save_all_and_get_all_contacts():
    storage = JSONStorage(TEST_FILE)

    contacts = [
        Contact(
            first_name="Lesya",
            last_name="Ukrainka",
            phones={"mobile": "12345"},
            contact_id="1",
        )
    ]

    storage.save_all(contacts)
    loaded = storage.get_all()

    assert len(loaded) == 1
    assert loaded[0].id == "1"
    assert loaded[0].first_name == "Lesya"
    assert loaded[0].phones["mobile"] == "12345"


def test_get_all_empty_file():
    with open(TEST_FILE, "w", encoding="utf-8") as f:
        f.write("")

    storage = JSONStorage(TEST_FILE)
    result = storage.get_all()

    assert result == []


def test_get_all_invalid_json():
    with open(TEST_FILE, "w", encoding="utf-8") as f:
        f.write("{invalid json}")

    storage = JSONStorage(TEST_FILE)
    result = storage.get_all()

    assert result == []
