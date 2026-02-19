# Phone Book CLI Application (Python)

A **Command Line Interface (CLI)** application for managing a phone book.  
Built with a **modular architecture**, **validated business logic**, **logging**, **automated tests**, 
and fully containerized using **Docker**.

---

## Features

- Add, update, and delete contacts
- Case-insensitive & fuzzy search (by name or phone number)
- UUID-based unique contact identifiers
- JSON file storage with error handling
- Automatic saving after changes
- Backup support before destructive operations
- Import contacts from CSV
- Export contacts to CSV
- Logging instead of print statements
- Fully tested with pytest
- Dependency management with Poetry
- Docker & Docker Compose support

---

## Project Structure

├── app/
│   ├── api.py        # Business logic
│   ├── cli.py        # CLI interface
│   ├── models.py     # Data models
│   ├── storage.py    # File storage (JSON, CSV, backups)
│   ├── utils.py      # Helpers & validation
│   └── logger.py     # Logging configuration
├── tests/            # Pytest test suite
├── data/             # JSON data, logs, backups
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── poetry.lock
├── main.py           # Application entry point
└── README.md

---

## CLI Interface

The application provides a simple and user-friendly CLI menu:

📞 PHONE BOOK MENU
1. Show all contacts
3. Search by last name
4. Search by phone number
5. Delete contact
6. Import from CSV
7. Export to CSV
8. Update contact
q. Exit
👉 Choose an action:

---

## Run Locally (Poetry)

1️⃣ Install dependencies
`poetry install`

2️⃣ Run the application
`poetry run python main.py`

3️⃣ Run tests
`poetry run pytest`

---

## Run with Docker

1️⃣ Build the image
`docker compose build`

2️⃣ Run the CLI application
`docker compose run app`

3️⃣ Run tests inside Docker
`docker compose run app pytest`

---

## Testing

Testing framework: pytest

Covered layers:
- models — contact creation and ID generation
- api — business logic (add, search, delete, update)
- storage — JSON/CSV persistence and backups
- utils — validation and formatting helpers

CLI and entry point (main.py) are intentionally not tested.

---

## Logging

The application uses Python’s built-in logging module.

Logs are written to:
data/phonebook.log

---

## Technologies Used

Python 3.10+
Poetry
Pytest
Docker & Docker Compose
JSON / CSV
UUID
Logging

