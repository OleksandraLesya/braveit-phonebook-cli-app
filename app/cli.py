# app/cli.py

"""
Command Line Interface for the Phone Book application.
"""

from app.api import PhoneBook
from app.models import Contact
from app.storage import JSONStorage
from app.utils import is_valid_phone, format_contact

DATA_FILE = "data/phonebook.json"


class PhoneBookCLI:
    """
    CLI interface for interacting with the Phone Book.
    """

    def __init__(self):
        storage = JSONStorage(DATA_FILE)
        self.phonebook = PhoneBook(storage)

    def run(self):
        while True:
            choice = self.menu()

            match choice:
                case "1":
                    self.show_contacts()
                case "2":
                    self.add_contact()
                case "3":
                    self.search_lastname()
                case "4":
                    self.search_phone()
                case "5":
                    self.delete_contact()
                case "8":
                    self.update_contact()
                case "q":
                    break

    def menu(self):
        print("\n📞 PHONE BOOK MENU")
        print("1. Show all contacts")
        print("2. Add contact")
        print("3. Search by last name")
        print("4. Search by phone")
        print("5. Delete contact")
        print("8. Update contact")
        print("q. Exit")
        return input("👉 Choose action: ").strip()

    def show_contacts(self):
        for c in self.phonebook.contacts:
            print(format_contact(c.to_dict()))

    def add_contact(self):
        first = input("First name: ")
        last = input("Last name: ")
        phone = input("Phone: ")

        if not is_valid_phone(phone):
            print("Invalid phone number")
            return

        contact = Contact(first, last, {"mobile": phone})
        self.phonebook.add_contact(contact)

    def delete_contact(self):
        cid = input("Contact ID: ")
        self.phonebook.delete_contact(cid)

    def update_contact(self):
        cid = input("Contact ID: ")
        contact = self.phonebook.find_by_id(cid)
        if not contact:
            print("Contact not found")
            return

        city = input(f"City [{contact.city}]: ").strip()
        updates = {}

        if city:
            updates["city"] = city.capitalize()

        if updates:
            self.phonebook.update_contact(cid, updates)

    def search_lastname(self):
        q = input("Last name: ")
        for c in self.phonebook.search_by_lastname(q):
            print(format_contact(c.to_dict()))

    def search_phone(self):
        q = input("Phone: ")
        for c in self.phonebook.search_by_phone(q):
            print(format_contact(c.to_dict()))
