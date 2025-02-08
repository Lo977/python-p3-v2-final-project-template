# Agent and Properties Management (CLI & Database)

## Learning Goals

✅ Understand Python Object-Oriented Programming (OOP) principles
✅ Implement one-to-many relationships in OOP
✅ Work with SQLite databases for data persistence
✅ Create a Command Line Interface (CLI) for user interaction
✅ Perform CRUD operations using Python
✅ Develop a structured, maintainable, and scalable Python project

---

## Introduction

Welcome to the Agent and Properties Management project! This Python based application allows users to manage real estate agents and their property listings efficiently using a command-line interface (CLI) and SQLite for persistent data storage. It demonstrates how to implement Object-Oriented Programming (OOP) principles in Python while handling a one-to-many relationship between agents and properties.it provides CRUD (Create, Read, Update, Delete) functionalities to track agents and their assigned properties.

## Features

- Command Line Interface (CLI) for user interaction
- One-to-Many Relationship (One agent can manage multiple properties)
- Persistent Data Storage using SQLite
- CRUD Operations (Create, Read, Update, Delete) for agents and properties
- Python OOP Implementation (Classes, Attributes, Methods, Inheritance)

## Purpose

This project is built as part of my Flatiron Phase-3 coursework to solidify my understanding of:

- Python OOP (Classes, Objects, Inheritance, Methods)
- SQLite Database (Data Persistence, Queries, CRUD Operations)
- CLI Applications (User Interaction via Terminal)

The goal is to create a simple yet practical tool for managing real estate agents and their assigned properties efficiently.

## How to Download and Run

- Clone the Repository
- Navigate to the Project Directory
- Install Dependencies( pip install)

## Important Files

- cli.py (CLI Entry Point)
  This script serves as the main entry point for the application. It initializes the CLI menu.Contains all CLI-related logic, including user input handling, displaying options, and calling appropriate functions from other modules to perform requested actions.

- helpers.py
  Acts as a middleware between the CLI and the database by handling data requests from models and providing formatted responses back to the CLI. It ensures that data retrieval, validation, and formatting are done efficiently, making the CLI more organized and user-friendly.

- agent.py
  Defines the Agent class, representing real estate agents. It includes methods for adding properties and retrieving all properties managed by an agent.

- property.py
  Defines the Property class, representing individual properties. Each property is associated with an agent, creating a one-to-many relationship.

## CLI Usage

- When you run the application, you will see the following options:
  Welcome to the Real Estate Management CLI!
  --- Main Menu ---

1. Manage Agents
2. Exit

3. List All Agents
4. Find Agent By Name
5. Add New Agent
6. Back to Main Menu
   Choose an option:

## Adding an Agent

Choose an option: 3
Enter agent's name: John Doe
Enter agent's email: John@mail.com
Enter agent's phone: 123-534-3432
Enter agent's dre_num: 234423
Agent John Doe added successfully!

Note: The directory also includes two files named `CONTRIBUTING.md` and
`LICENSE.md` that are specific to Flatiron's curriculum. You can disregard or
delete the files if you want.

---

## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---

## Generating Your CLI

A CLI is, simply put, an interactive script and prompts the user and performs
operations based on user input.

The project template has a sample CLI in `lib/cli.py` that looks like this:

```py
# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
```

The helper functions are located in `lib/helpers.py`:

```py
# lib/helpers.py

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
```

You can run this CLI with `python lib/cli.py`. The template CLI will ask for input, do
some work, and accomplish some sort of task.

## Conclusion

This project is a stepping stone in masterring Python,database and CLI development. it showcases how real-world applications can be built with OOP principles and SQLite databasee.This project offers a structured apporoach to learning Python's OOP capabilities while building something practical.

Happy coding!

---
