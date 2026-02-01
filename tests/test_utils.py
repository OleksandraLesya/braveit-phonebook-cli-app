# tests/test_utils.py

from app.utils import (
    is_valid_phone,
    normalize_text,
    fuzzy_match,
    format_contact,
)


def test_is_valid_phone():
    assert is_valid_phone("12345") is True
    assert is_valid_phone("123abc") is False
    assert is_valid_phone("") is False


def test_normalize_text():
    assert normalize_text("  HeLLo ") == "hello"


def test_fuzzy_match():
    assert fuzzy_match("les", "Lesya") is True
    assert fuzzy_match("abc", "Lesya") is False


def test_format_contact_returns_string():
    contact = {
        "id": "123",
        "first_name": "Lesya",
        "last_name": "Ukrainka",
        "phones": {"mobile": "12345"},
        "city": "Kyiv",
        "job": "QA",
        "created_at": "2025-01-01",
    }

    result = format_contact(contact)

    assert isinstance(result, str)
    assert "Lesya Ukrainka" in result
    assert "12345" in result
