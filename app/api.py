# app/api.py

"""
Бізнес-логіка (API) для застосунку Phone Book CLI.

Цей модуль надає чисті функції для:
- додавання, видалення, оновлення контактів
- пошуку контактів (включаючи нечіткий пошук)
- тут заборонено використовувати calls input() або print()
"""

from typing import List, Optional
from difflib import get_close_matches
from app.logger import logger


def find_contact_by_id(phonebook: List[dict], contact_id: str) -> Optional[dict]:
    """
    Шукає контакт у телефонній книзі за його унікальним ID.

    :param phonebook: список контактів
    :param contact_id: ID контакту
    :return: словник контакту або None, якщо не знайдено
    """
    return next((c for c in phonebook if c["id"] == contact_id), None)


def add_contact(phonebook: List[dict], contact: dict) -> bool:
    """
    Додає новий контакт до телефонної книги.

    :param phonebook: список контактів
    :param contact: словник нового контакту
    :return: False, якщо контакт з таким ID вже існує, інакше True
    """
    if find_contact_by_id(phonebook, contact["id"]):
        logger.warning("Контакт з таким ID вже існує.")
        return False

    phonebook.append(contact)
    logger.info(
        "Контакт додано: %s %s",
        contact.get("first_name"),
        contact.get("last_name"),
    )
    return True


def delete_contact(phonebook: List[dict], contact_id: str) -> bool:
    """
    Видаляє контакт за його унікальним ID.

    :param phonebook: список контактів
    :param contact_id: ID контакту для видалення
    :return: True, якщо видалено успішно, False, якщо не знайдено
    """
    contact = find_contact_by_id(phonebook, contact_id)

    if not contact:
        logger.warning("Контакт не знайдено для видалення.")
        return False

    phonebook.remove(contact)
    logger.info("Контакт видалено: %s", contact_id)
    return True


def update_contact(phonebook: List[dict], contact_id: str, updates: dict) -> bool:
    """
    Оновлює поля існуючого контакту за його ID.

    :param phonebook: список контактів
    :param contact_id: ID контакту для оновлення
    :param updates: словник з новими даними
    :return: True, якщо оновлено успішно, інакше False
    """
    contact = find_contact_by_id(phonebook, contact_id)

    if not contact:
        logger.warning("Контакт не знайдено для оновлення.")
        return False

    contact.update(updates)
    logger.info("Контакт оновлено: %s", contact_id)
    return True


def search_by_lastname(phonebook: List[dict], query: str) -> List[dict]:
    """
    Виконує нечіткий (fuzzy) пошук контактів за прізвищем.

    :param phonebook: список контактів
    :param query: запит (прізвище)
    :return: список знайдених контактів
    """
    lastnames = [c.get("last_name", "") for c in phonebook]
    matches = get_close_matches(query.capitalize(), lastnames, cutoff=0.6)

    return [c for c in phonebook if c.get("last_name") in matches]


def search_by_phone(phonebook: List[dict], query: str) -> List[dict]:
    """
    Шукає контакти за входженням номера телефону (підрядок).

    :param phonebook: список контактів
    :param query: частина номера телефону
    :return: список знайдених контактів
    """
    return [
        c for c in phonebook
        if any(query in str(number) for number in c.get("phones", {}).values())
    ]
