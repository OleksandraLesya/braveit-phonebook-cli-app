# appmodels.py

"""
Моделі даних для застосунку Phone Book CLI.

Цей модуль відповідає за:
- створення сутностей контактів
- генерацію унікальних ідентифікаторів (ID)
- нормалізацію та валідацію необроблених вхідних даних

Модель контакту представлена у вигляді словника, щоб проект
залишався легким і зрозумілим для початківців.
"""

import uuid
from datetime import datetime
from typing import Dict


def generate_id() -> str:
    """
    Генерує унікальний UUID для контакту.

    :return: рядок UUID
    """
    return str(uuid.uuid4())


def create_contact(
    first_name: str,
    last_name: str,
    phones: Dict[str, str],
    city: str = "",
    job: str = ""
) -> dict:
    """
    Створює новий контакт телефонної книги.

    :param first_name: ім'я
    :param last_name: прізвище
    :param phones: словник телефонів (mobile, home тощо)
    :param city: місто
    :param job: професія
    :return: словник контакту
    """
    return {
        "id": generate_id(),
        "first_name": first_name.strip().capitalize(),
        "last_name": last_name.strip().capitalize(),
        "phones": phones,
        "city": city.strip().capitalize(),
        "job": job.strip().capitalize(),
        "created_at": datetime.now().isoformat()
    }
