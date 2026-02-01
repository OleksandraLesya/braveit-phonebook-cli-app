# app/storage.py

"""
Шар збереження даних для застосунку Phone Book CLI.

Цей модуль керує:
- завантаженням даних телефонної книги з JSON
- збереженням даних телефонної книги в JSON
- створенням резервних копій (backup) телефонної книги

Він не містить бізнес-логіки.
"""

import json
import os
import shutil
from typing import List
from app.logger import logger


def load_phonebook(filename: str) -> List[dict]:
    """
    Завантажує телефонну книгу з JSON-файлу.
    """
    if not os.path.exists(filename):
        logger.warning("Файл не знайдено. Створюється нова телефонна книга.")
        return []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                logger.warning("JSON файл порожній. Використовується порожня книга.")
                return []
            return json.loads(content)

    except json.JSONDecodeError:
        logger.error("JSON файл пошкоджений. Використовується порожня книга.")
        return []


def save_phonebook(filename: str, phonebook: List[dict]) -> None:
    """
    Зберігає телефонну книгу у JSON-файл.

    :param filename: шлях до файлу
    :param phonebook: список контактів
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(phonebook, file, indent=4, ensure_ascii=False)
    logger.info("Телефонну книгу збережено.")


def backup_phonebook(src: str, backup: str) -> None:
    """
    Створює резервну копію телефонної книги за допомогою shutil.
    """
    if os.path.exists(src):
        try:
            shutil.copy2(src, backup)
            logger.info("Backup створено: %s", backup)
        except Exception as e:
            logger.error("Помилка при створенні backup: %s", e)
