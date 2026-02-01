# app/logger.py

"""
Конфігурація логування для застосунку Phone Book CLI.

Цей модуль налаштовує:
- логування в консоль
- логування у файл (data/phonebook.log)
- єдиний логер, який використовується в усьому застосунку

Логер слід імпортувати в інші модулі, а не налаштовувати заново.
"""

import logging
import os

if not os.path.exists('data'):
    os.makedirs('data')

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("data/phonebook.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("PhoneBookApp")
