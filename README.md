# Phone Book CLI Application (OOP)

A **Command Line Interface (CLI)** application for managing a phone book.

The project was originally implemented in a procedural style and later refactored 
to an **Object-Oriented architecture** with a clear separation of concerns, with repository abstraction and constructor-based dependency injection.

Built with validated business logic, logging, automated tests, and fully containerized using Docker.

---

## Features

- ## Features

- Add, update, and delete contacts
- Case-insensitive & fuzzy search (by name or phone number)
- UUID-based unique contact identifiers
- JSON file storage with error handling
- Automatic timestamped backups before overwriting data
- Repository pattern for storage abstraction
- Constructor-based dependency injection
- Automatic persistence after changes
- Import contacts from CSV
- Export contacts to CSV
- Structured logging instead of print statements
- Fully tested with pytest
- Dependency management with Poetry
- Docker & Docker Compose support

---

## Architecture Overview

The application follows a layered structure:

- **Contact (models.py)** — domain model
- **PhoneBook (api.py)** — business logic layer
- **ContactRepository (repository.py)** — storage abstraction
- **JSONStorage (storage.py)** — file-based implementation
- **CLI (cli.py)** — user interaction layer
- **Logger (logger.py)** — centralized logging
- **Utils (utils.py)** — validation & formatting helpers

This separation improves testability, flexibility, and maintainability.

---

## Project Structure

├── app/
│   ├── api.py          # PhoneBook business logic
│   ├── cli.py          # CLI interface
│   ├── models.py       # Contact domain model
│   ├── repository.py   # Repository abstraction
│   ├── storage.py      # JSON/CSV storage & backups
│   ├── utils.py        # Helpers & validation
│   └── logger.py       # Logging configuration
├── tests/              # Pytest test suite
├── data/               # JSON data, logs, backups
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── poetry.lock
├── main.py             # Application entry point
└── README.md

---

## CLI Interface

The application provides a simple and user-friendly CLI menu:

📞 PHONE BOOK MENU
1. Show all contacts
2. Add contacts
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
- models — contact creation and ID handling
- api — business logic (add, search, delete, update)
- storage — JSON repository implementation with backup support
- utils — validation and formatting helpers

CLI and entry point (main.py) are intentionally not tested.

---

## Logging

The application uses Python’s built-in logging module.

Logs are written to:
data/phonebook.log

---

## Technologies Used

- Python 3.10+
- Poetry
- Pytest
- Docker & Docker Compose
- JSON / CSV
- UUID
- Logging

## Design Principles

- Separation of Concerns
- Repository Pattern
- Dependency Injection
- Layered Architecture
- Test Isolation via FakeRepository