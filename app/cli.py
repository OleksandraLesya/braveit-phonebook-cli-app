# app/cli.py

"""
Інтерфейс командного рядка (CLI) для застосунку Phone Book.

Керує:
- взаємодією з користувачем
- меню
- імпортом/експортом CSV
- викликом функцій API та шарів збереження даних
"""

import csv
from app.storage import load_phonebook, save_phonebook
from app.models import create_contact
from app.api import (
    add_contact,
    delete_contact,
    update_contact,
    search_by_lastname,
    search_by_phone,
)
from app.utils import is_valid_phone, format_contact

DATA_FILE = "data/phonebook.json"

def menu() -> str:
    """Відображає головне меню та повертає вибір користувача."""
    print("\n📞 PHONE BOOK MENU")
    print("1. Показати всі контакти")
    print("2. Додати контакт")
    print("3. Пошук за прізвищем")
    print("4. Пошук за номером")
    print("5. Видалити контакт")
    print("6. Імпорт з CSV")
    print("7. Експорт у CSV")
    print("8. Оновити контакт")
    print("q. Вийти")

    return input("👉 Оберіть дію: ").strip()

def show_contacts(phonebook):
    """Виводить усі контакти в консоль."""
    if not phonebook:
        print("Телефонна книга порожня")
        return

    for contact in phonebook:
        print("-" * 40)
        print(format_contact(contact))

def add_new_contact(phonebook):
    """Діалог створення нового контакту."""
    first_name = input("Імʼя: ")
    last_name = input("Прізвище: ")
    phone = input("Мобільний номер: ")

    if not is_valid_phone(phone):
        print("Невірний номер")
        return

    contact = create_contact(
        first_name=first_name,
        last_name=last_name,
        phones={"mobile": phone},
    )

    if add_contact(phonebook, contact):
        # Порада: зберігаємо відразу після додавання (Auto-save)
        save_phonebook(DATA_FILE, phonebook)
        print("Контакт успішно додано")

def import_csv(phonebook):
    """Діалог імпорту контактів з файлу CSV."""
    path = input("Шлях до CSV (наприклад, data/phonebook.csv): ")
    try:
        with open(path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contact = create_contact(
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    phones={"mobile": row["phone"]},
                    city=row.get("city", ""),
                    job=row.get("job", "")
                )
                add_contact(phonebook, contact)
        save_phonebook(DATA_FILE, phonebook)
        print("CSV імпорт завершено")
    except FileNotFoundError:
        print("Файл не знайдено")

def export_csv(phonebook):
    """Експортує поточну книгу у CSV файл."""
    path = input("Зберегти CSV як (наприклад, data/export.csv): ")
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["first_name", "last_name", "phone", "city", "job"])

        for c in phonebook:
            # Беремо перший доступний номер телефону
            phone_val = list(c["phones"].values())[0] if c["phones"] else ""
            writer.writerow([
                c["first_name"],
                c["last_name"],
                phone_val,
                c["city"],
                c["job"]
            ])
    print(f"CSV експорт завершено у файл: {path}")

def update_existing_contact(phonebook):
    """
    Діалог оновлення існуючого контакту.
    Користувач може пропустити будь-яке поле (Enter).
    """
    cid = input("Введіть ID контакту для оновлення: ").strip()

    contact = next((c for c in phonebook if c["id"] == cid), None)
    if not contact:
        print("Контакт не знайдено")
        return

    print("Залиште поле порожнім, щоб не змінювати його")

    first_name = input(f"Імʼя [{contact['first_name']}]: ").strip()
    last_name = input(f"Прізвище [{contact['last_name']}]: ").strip()
    city = input(f"Місто [{contact['city']}]: ").strip()
    job = input(f"Професія [{contact['job']}]: ").strip()
    phone = input(
        f"Мобільний номер [{contact['phones'].get('mobile', '')}]: "
    ).strip()

    updates = {}

    if first_name:
        updates["first_name"] = first_name.capitalize()
    if last_name:
        updates["last_name"] = last_name.capitalize()
    if city:
        updates["city"] = city.capitalize()
    if job:
        updates["job"] = job.capitalize()

    if phone:
        if not is_valid_phone(phone):
            print("Невірний номер телефону")
            return
        updates["phones"] = {**contact["phones"], "mobile": phone}

    if not updates:
        print("Нічого не змінено")
        return

    if update_contact(phonebook, cid, updates):
        save_phonebook(DATA_FILE, phonebook)
        print("Контакт успішно оновлено")


def run():
    """Головний цикл роботи програми."""
    phonebook = load_phonebook(DATA_FILE)

    while True:
        choice = menu()

        match choice:
            case "1":
                show_contacts(phonebook)
            case "2":
                add_new_contact(phonebook)
            case "3":
                q = input("Прізвище (або частина): ")
                results = search_by_lastname(phonebook, q)
                if results:
                    for c in results:
                        print(format_contact(c))
                else:
                    print("Нічого не знайдено")
            case "4":
                q = input("Номер (або частина): ")
                results = search_by_phone(phonebook, q)
                if results:
                    for c in results:
                        print(format_contact(c))
                else:
                    print("Нічого не знайдено")
            case "5":
                cid = input("Введіть ID контакту для видалення: ")
                if delete_contact(phonebook, cid):
                    save_phonebook(DATA_FILE, phonebook)
                    print("Видалено")
                else:
                    print("Контакт не знайдено")
            case "6":
                import_csv(phonebook)
            case "7":
                export_csv(phonebook)
            case "8":
                update_existing_contact(phonebook)
            case "q":
                save_phonebook(DATA_FILE, phonebook)
                print("До побачення!")
                break
            case _:
                print("Невірний вибір, спробуйте ще раз.")
               