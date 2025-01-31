# lib/cli.py

from helpers import (
    manage_agent,
    main_menu,
    exit_program,
    create_agent,
    list_agents,
    # agent_management_menu,
    # find_agent_by_id,
    # find_by_name,
    update_agent,
    delete_agent,
    agent_menu

)

# def main_menu():
#     print("\n Welcome to the Real Estate Management CLI!")
   
#     print("--- Main Menu ---")
#     print("-------------------------")
#     print("1. Manage Agents")
#     print("2. Manage Properties")
#     print("0. Exit")



# def agent_profile_menu():
#     print("Type U or u tp Update Agent's profile.")
#     print("Type D or d to Delete Agent's profile.")






# def main():
#     while True:
#         menu()
#         choice = input("> ")
#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             create_agent()
#         elif choice == "2":
#             list_agents()
#         elif choice == "3":
#             find_agent_by_id()
#         elif choice == "4":
#             find_by_name()
#         elif choice == "5":
#             update_agent()
#         elif choice == "6":
#             delete_agent()
#         else:
#             print("Invalid choice")


# def menu():
#     print("Please select an option:")
#     print("0. Exit the program")
#     print("1. Create Agent")
#     print("2. List All Agent")
#     print("3. Find Agent By Id")
#     print("4. find Agent by Name")
#     print("5. Update Agent")
#     print("6. Delete Agent")

def run_cli():
    choice = ""
    while choice != "0":
        main_menu()
        choice = input("> ")

        if choice == "1":
            manage_agent()
        elif choice == "2":
            print("Manage properties functionality is not inplemented yet.")
        elif choice == "0":
            print("Exitting The Progam...")  
            exit()
        else:
            print("Invalid choice! Please try again.")
          
            
if __name__ == "__main__":
    run_cli()
