# lib/cli.py

from helpers import (
    exit_program,
    create_agent,
    get_all_agents,
    update_agent,
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

        choice = input("> ").strip()
        if choice == "1":
            list_agents_cli()
            pass
        elif choice == "2":
            pass
            # find_agent_by_name()
        elif choice == "3":
            pass
            create_agent_cli()
        elif choice != "0":
            print("Invalid Input! Please enter a valid number.")
        # else:
    print("Exitting back to main menu")    

def create_agent_cli():
    name = input("Enter Agent's Name: ").title()
    email = input("Enter Agent's Email: ").lower()
    phone = input("Enter Agent's Phone: ")
    dre_num = int(input("Enter Agent's dre_num: "))   

    agent = create_agent(name,email,phone,dre_num)
    print(f"✅ Agent {agent.name} created successfully!")

def list_agents_cli():
    agents = get_all_agents()
    if not agents:
        print("\nNo agents found.\n")
    print(f"\n-- List of Agents --\n")
    for i,agent in enumerate(agents,start=1):
        print(f"{i}.{agent.name}")
    
    selected_index = int(input("\n-- Enter an agent by number to view details or modify (0 To go back): "))
    if selected_index == 0:
        return None
    elif 1<= selected_index <= len(agents):
        return agent_options(agents[selected_index - 1])
    else:
        print("Invalid selection")
        return None
    
def agent_options(agent):
    choice = ""
    while choice !="0":
        print(f"\n Agent: {agent.name}, Email: {agent.email}, Phone: {agent.phone}, DRE# : {agent.dre_num}")
        print(f"\n1. Update Agent")
        print(f"2. Delete Agent")
        print(f"3. Add Property")
        print(f"4. List Properties")
        print(f"0. Back to Previous Menu")

        choice = input("> ").strip()

        if choice == "1":
            update_agent_cli(agent)
        elif choice == "2":
            # delete agent
            pass
            choice = "0"
        elif choice == "3":
            # add properties
            pass
        elif choice == "4":
            # list properties
            pass
        elif choice !="0":
            print("Invalid input. Please try again.")

def update_agent_cli(agent):
    print(f"\nUpdating Agent: {agent.name}")
    agent.name = input(f"\nEnte new name ( or press Enter to keep {agent.name}): ").title() or agent.name
    agent.email = input(f"Enter new email (or press Enter to keep {agent.email})").lower() or agent.email
    agent.phone = input(f"Enter new phone number (or press Enter to keep {agent.phone})") or agent.phone
    agent.dre_num = input(f"Enter new DRE # (or press Enter to keep {agent.dre_num}") or agent.dre_num

    confirmation = input(f"Are you sure you want to update this agent: {agent.name} ? (Y/N): ").strip().lower()
    if confirmation == "y":
        update_agent(agent)
        print(f"\n✅ Agent {agent.name} updated successfully.")
    else:
         print("\n❌ Agent Update canceled.")

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