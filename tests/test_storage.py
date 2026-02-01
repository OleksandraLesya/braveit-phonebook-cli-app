# tests/test_storage.py

import os
from app.storage import load_phonebook, save_phonebook

TEST_FILE = "data/test_phonebook.json"


def teardown_function():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_load_phonebook_file_not_exists():
    result = load_phonebook("data/no_such_file.json")
    assert result == []


def test_save_and_load_phonebook():
    phonebook = [
        {
            "id": "1",
            "first_name": "Lesya",
            "last_name": "Ukrainka",
            "phones": {"mobile": "12345"},
        }
    ]

    save_phonebook(TEST_FILE, phonebook)
    loaded = load_phonebook(TEST_FILE)

    assert loaded == phonebook


def test_load_phonebook_empty_file():
    with open(TEST_FILE, "w", encoding="utf-8") as f:
        f.write("")

    result = load_phonebook(TEST_FILE)
    assert result == []


def test_load_phonebook_invalid_json():
    with open(TEST_FILE, "w", encoding="utf-8") as f:
        f.write("{invalid json}")

    result = load_phonebook(TEST_FILE)
    assert result == []
