from models.agent import Agent
from models.property import Property


def exit_program():
    print("Goodbye!")
    exit()


def main_menu():
    # while True:
        print("\nWelcome to the Real Estate Management CLI!")
        print("--- Main Menu ---")
        print("1. Manage Agents")
        print("2. Manage Properties")
        print("0. Exit")

        # choice = input("> ")
        # if choice == "1":
        #     manage_agent()
        # elif choice == "2":
        #     manage_properties()
        # elif choice == "0":
        #     exit_program()
        # else:
        #     print("Invalid input, please try again.")


def manage_agent():
    while True:
        print("\n-- Agents Management --")
        print("1. List All Agents")
        print("2. Find Agent By Name")
        print("3. Add New Agent")
        print("0. Back to Main Menu")

        choice = input("> ")
        if choice == "1":
            list_agents()
        elif choice == "2":
            find_agent_by_name()
        elif choice == "3":
            create_agent()
        elif choice == "0":
            return
        else:
            print("Invalid Input! Please enter a valid number.")


def list_agents():
    agents = Agent.get_all()
    if not agents:
        print("No agents found!")
        return

    print("\n--- List of Agents ---")
    for index, agent in enumerate(agents, start=1):
        print(f"{index}. {agent.name}")

    while True:
        try:
            selected_index = int(input("\nEnter agent number to manage (or 0 to go back): "))
            if selected_index == 0:
                return
            elif 1 <= selected_index <= len(agents):
                agent_menu(agents[selected_index - 1])
                return  # Ensures we exit after agent_menu
            else:
                print("Invalid selection. Try again.")
        except ValueError:
            print("Please enter a valid number.")


def agent_menu(agent):
    while True:
        print(f"\n--- Managing Agent {agent.name} ---")
        print("1. Update Agent")
        print("2. Delete Agent")
        print("3. Add Property")
        print("4. List Properties")
        print("0. Back to Agent Management")

        choice = input("> ")
        if choice == "1":
            update_agent(agent)
        elif choice == "2":
            if delete_agent(agent):  # If deleted, exit the function
                return
        elif choice == "3":
            add_property_for_agent(agent)
        elif choice == "4":
            list_agent_properties(agent)
        elif choice == "0":
            return
        else:
            print("Invalid input. Please enter a valid number.")


def create_agent():
    name = input("Enter Agent's name: ").title()
    email = input("Enter Agent's email: ").lower()
    phone = input("Enter Agent's phone #: ")
    dre_num = int(input("Enter Agent's DRE #: "))

    try:
        agent = Agent.create(name, email, phone, dre_num)
        print(f"\n✅ Agent {agent.name} created successfully.")
    except Exception as e:
        print(f"❌ Error creating Agent: {e}")


def find_agent_by_name():
    name = input("Enter Agent's Name: ").title()
    agent = Agent.find_by_name(name)

    if agent:
        print(f"\n--- Agent Found ---")
        print(f"Name: {agent.name}, Email: {agent.email}, Phone: {agent.phone}, DRE: {agent.dre_num}")
        agent_menu(agent)
    else:
        print(f"Agent '{name}' not found.")


def update_agent(agent):
    print(f"\n--- Updating Agent: {agent.name} ---")

    agent.name = input(f"Enter new name (or press Enter to keep {agent.name}): ").title() or agent.name
    agent.email = input(f"Enter new email (or press Enter to keep {agent.email}): ").lower() or agent.email
    agent.phone = input(f"Enter new phone (or press Enter to keep {agent.phone}): ") or agent.phone
    agent.dre_num = input(f"Enter new DRE# (or press Enter to keep {agent.dre_num}): ") or agent.dre_num

    confirmation = input("Are you sure you want to update this agent? (Y/N): ").strip().lower()
    if confirmation == "y":
        agent.update()
        print(f"\n✅ Agent {agent.name} updated successfully.")
    else:
         print("\n❌ Agent Update canceled.")


def delete_agent(agent):
    confirmation = input(f"Are you sure you want to delete Agent {agent.name}? (Y/N): ").strip().lower()
    if confirmation == "y":
        agent.delete()
        print(f"\n✅ Agent {agent.name} deleted successfully.")
        return True  # Return True to indicate successful deletion
    else:
        print("❌ Agent Deletion canceled.")
        return False


def add_property_for_agent(agent):
    print(f"\n--- Adding Property for Agent: {agent.name} ---")
    address = input("Enter Property Address: ")
    price = int(input("Enter Property price: "))

    confirmation = input(f"\nAre you sure you want to add this property for Agent {agent.name}? (Y/N) ").lower()
    if confirmation == "y":
        property = Property(address, price, agent.id)
        property.save()
        print(f"\n✅ Property added successfully.")
    else:
        print("\n❌ Property addition canceled.")


def list_agent_properties(agent):
    properties = Property.get_properties_by_agent(agent.id)
    # properties = agent.properties()
    if not properties:
        print(f"\n-- {agent.name} has no properties listed. --")
        return

    print(f"\n--- Properties for {agent.name} ---")
    for idx, property in enumerate(properties, start=1):
        print(f"{idx}. Address: {property.address}, Price: ${property.price}.00")

    while True:
        try:
            selected_index = int(input("\nSelect property number for options (or 0 to go back): "))
            if selected_index == 0:
                return
            elif 1 <= selected_index <= len(properties):
                property_options(properties[selected_index - 1])
            else:
                print("Invalid selection. Try again.")
        except ValueError:
            print("Please enter a valid number.")


def property_options(property):
    choice = ""
    while choice !="0":
    # while True:
        print(f"\n--- Property: {property.address} ---")
        print("1. Update Property")
        print("2. Delete Property")
        print("0. Back to Previous Menu")

        choice = input("> ").strip()
        if choice == "1":
            update_property(property)
        elif choice == "2":
            if delete_property(property):
                choice = "0"
                # return  # If deleted, exit property menu
        # elif choice == "0":
            # return
        elif choice !="0":
            print("Invalid input. Try again.")


def update_property(property):
    address = input(f"Enter new address (or press Enter to keep {property.address}): ") or property.address
    price = input(f"Enter new price (or press Enter to keep {property.price}): ") or property.price

    confirmation = input("Are you sure you want to update this property? (Y/N): ").lower()
    if confirmation == "y":
        property.address = address
        property.price = int(price)
        property.update()
        print("\n✅ Property updated successfully.")
    else:
        print("\n❌ Property update canceled.")


def delete_property(property):
    confirmation = input(f"Are you sure you want to delete {property.address}? (Y/N): ").lower()
    if confirmation == "y":
        property.delete()
        print("\n✅ Property deleted successfully.")
        return True
    else:
        print("\n❌ Property deletion canceled.")
        return False


# Start the program
# main_menu()
