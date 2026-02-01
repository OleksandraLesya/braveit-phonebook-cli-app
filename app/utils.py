# app/utils.py

"""
Допоміжні функції (утиліти) для застосунку Phone Book CLI.

Цей модуль містить функції, які повторно використовуються в усьому застосунку:
- валідація номерів телефонів
- форматування контактів для відображення
- невелика логіка без побічних ефектів

Тут не повинні виконуватися операції вводу/виводу (input/output).
"""

import csv
from typing import Dict, List


def is_valid_phone(number: str) -> bool:
    """
    Перевіряє, чи номер телефону складається лише з цифр
    та не є порожнім.

    :param number: номер телефону
    :return: True, якщо номер валідний
    """
    return number.isdigit() and len(number) >= 5


def normalize_text(text: str) -> str:
    """
    Нормалізує текст для порівняння (lowercase + strip).

    :param text: вхідний текст
    :return: нормалізований текст
    """
    return text.strip().lower()


def format_contact(contact: Dict) -> str:
    """
    Повертає гарно відформатований контакт для CLI.

    :param contact: словник контакту
    :return: форматований рядок
    """
    phones = ", ".join(
        f"{k}: {v}" for k, v in contact.get("phones", {}).items()
    )

    return (
        f"Ім'я: {contact.get('first_name', '')} {contact.get('last_name', '')}\n"
        f"Телефони: {phones}\n"
        f"Місто: {contact.get('city', '')}\n"
        f"Професія: {contact.get('job', '')}\n"
        f"ID: {contact.get('id', '')}\n"
        f"Створено: {contact.get('created_at', '')}"
    )


def fuzzy_match(query: str, text: str) -> bool:
    """
    Виконує нечітке (fuzzy) порівняння рядків.

    :param query: пошуковий запит
    :param text: текст для порівняння
    :return: True, якщо query входить у text
    """
    return normalize_text(query) in normalize_text(text)


def export_to_csv(phonebook: List[Dict], filename: str) -> None:
    """
    Експортує телефонну книгу у CSV-файл.

    :param phonebook: список контактів
    :param filename: шлях до CSV-файлу
    """
    if not phonebook:
        return

    fieldnames = [
        "id",
        "first_name",
        "last_name",
        "phones",
        "city",
        "job",
        "created_at",
    ]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for contact in phonebook:
            row = contact.copy()
            row["phones"] = "; ".join(
                f"{k}:{v}" for k, v in contact.get("phones", {}).items()
            )
            writer.writerow(row)


def import_from_csv(filename: str) -> List[Dict]:
    """
    Імпортує контакти з CSV-файлу.

    :param filename: шлях до CSV-файлу
    :return: список контактів
    """
    contacts: List[Dict] = []

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            phones = {}
            if row.get("phones"):
                for item in row["phones"].split(";"):
                    if ":" in item:
                        k, v = item.split(":", 1)
                        phones[k.strip()] = v.strip()

            contacts.append(
                {
                    "id": row.get("id", ""),
                    "first_name": row.get("first_name", ""),
                    "last_name": row.get("last_name", ""),
                    "phones": phones,
                    "city": row.get("city", ""),
                    "job": row.get("job", ""),
                    "created_at": row.get("created_at", ""),
                }
            )

    return contacts
