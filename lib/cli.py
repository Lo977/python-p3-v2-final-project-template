# lib/cli.py

from helpers import (
    exit_program,
)

def main_menu():
    print("\n Welcome to the Real Estate Management CLI!")
   
    print("--- Main Menu ---")
    print("-------------------------")
    print("1. Manage Agents")
    print("0. Exit")
def manage_agent():
    choice = ""
    while choice != "0":
        print("\n-- Agents Management --")
        print("1. List All Agents")
        print("2. Find Agent By Name")
        print("3. Add New Agent")
        print("0. Back to Main Menu")

        choice = input("> ")
        if choice == "1":
            # list_agents()
            pass
        elif choice == "2":
            pass
            # find_agent_by_name()
        elif choice == "3":
            pass
            # create_agent()
        elif choice != "0":
            print("Invalid Input! Please enter a valid number.")
        # else:
    print("Exitting back to main menu")       

def run_cli():
    choice = ""
    while choice != "0":
        main_menu()
        choice = input("> ").strip()

        if choice == "1":
            manage_agent()
            pass
        elif choice == "2":
            print("Manage properties functionality is not inplemented yet.")
        # elif choice == "0":
        #     print("Exitting The Progam...")  
        #     exit_program()
        elif choice !="0":
            print("Invalid choice! Please try again.")
    print("Exitting The Progam...\n Good Bye!")  
    exit_program()      
            
if __name__ == "__main__":
    run_cli()