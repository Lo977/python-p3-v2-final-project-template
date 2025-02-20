# Agent and Properties Management (CLI & Database)

This project is structured using Object-Oriented Programming (OOP) and Object-Relational Mapping (ORM) to facilitate seamless interaction with the database.

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

- Python OOP (Classes, Objects, Attributes, Methods)
- SQLite Database (Data Persistence, Queries, CRUD Operations)
- CLI Applications (User Interaction via Terminal)

The goal is to create a simple yet practical tool for managing real estate agents and their assigned properties efficiently.

## How it works

Users interact with the CLI through a series of text-based menus. The application provides functionalities to:

- Manage real estate agents (Create, Read, Update, Delete).
- List, add, and modify properties associated with agents.
- Prevent duplicate agent registrations by checking for unique DRE numbers.
- Persist data using SQLite, ensuring all records are stored securely.

## Table of Contents

- Installation
- Usage
- CLI Script (cli.py)
- Helper Functions (helpers.py)
- Agent Model (agent.py)
- Property Model (property.py)
- Database Configuration (models/**init**.py)

## Installation

Ensure you have the following installed:
✅ Python 3.8+
✅ SQLite (comes pre-installed with Python)

## Usage

Once you run python lib/cli.py, you will be greeted with a menu-driven interface.

Welcome to the Real Estate Management CLI!

1. Manage Agents
2. Exit
   Users can navigate through numbered menu options to manage agents and properties.

## CLI Script (cli.py)

The cli.py file is the entry point of the application. It handles user input, menu navigation, and function calls.
Key Features
✅ Displays a structured menu.
✅ Calls helper functions to process CRUD operations.
✅ Handles invalid inputs and guides users effectively.

def main_menu():
print("\nWelcome to the Real Estate Management CLI!")
print("1. Manage Agents")
print("0. Exit")

Enter an option: 1
-- Agents Management --

1. List All Agents
2. Find Agent by Name
3. Add New Agent
4. Back to Main Menu

## Helper Functions (helpers.py)

This file contains utility functions that support the CLI by handling agent and property operations.
Key Functions
✅ create_agent(name, email, phone, dre_num) → Creates and saves a new agent.
✅ get_all_agents() → Retrieves all agents from the database.
✅ add_property(address, price, agent) → Assigns a new property to an agent.
✅ list_properties(agent) → Displays all properties owned by a specific agent.
✅ find_agent_by_name() → Searches for an agent by name.

def find_agent_by_name():
name = input("Enter Agent's name: ").title()
agent = Agent.find_by_name(name)
if agent:
print(f"\nAgent found: {agent.name}, Email: {agent.email}, Phone: {agent.phone}")
else:
print(f"❌ Agent '{name}' not found.")

## Agent Model (agent.py)

The Agent model defines the structure of real estate agents and interacts with the database.
Class: Agent
✅ Attributes: id, name, email, phone, dre_num
✅ Ensures Unique DRE Numbers: Prevents duplicate agent creation.
✅ CRUD Operations: save(), update(), delete(), get_all(), find_by_name()

def save(self):
sql = "SELECT \* FROM agents WHERE dre_num = ?"
existing_agent = CURSOR.execute(sql, (self.dre_num,)).fetchone()
if existing_agent:
print("\n❌ An agent with this DRE number already exists.")
return None

    sql = "INSERT INTO agents (name, email, phone, dre_num) VALUES (?, ?, ?, ?)"
    CURSOR.execute(sql, (self.name, self.email, self.phone, self.dre_num))
    CONN.commit()
    self.id = CURSOR.lastrowid

## Property Model (property.py)

The Property model stores real estate listings and links them to agents.

Class: Property
✅ Attributes: id, address, price, agent_id
✅ CRUD Operations: save(), update(), delete()
✅ Links to Agents via agent_id as a foreign key.

def properties(self):
sql = "SELECT \* FROM properties WHERE agent_id = ?"
rows = CURSOR.execute(sql, (self.id,)).fetchall()
return [Property.instance_from_db(row) for row in rows]

## Database Configuration(models/**init**.py)

This file initializes the database connection and defines global variables.

Key Components
✅ CONN → Establishes a connection to SQLite.
✅ CURSOR → Executes SQL commands.
✅ Creates necessary tables on startup.

import sqlite3

CONN = sqlite3.connect("real_estate.db")
CURSOR = CONN.cursor()

## How to Download and Run

- Clone the Repository
- Navigate to the Project Directory
- Install Dependencies( pip install)

## License

Developed by: Buddha Lo

## Conclusion

This project is a stepping stone in masterring Python,database and CLI development. it showcases how real-world applications can be built with OOP principles and SQLite databasee.This project offers a structured apporoach to learning Python's OOP capabilities while building something practical.

Happy coding!

---
