# lib/helpers.py

from models.agent import Agent
from models.property import Property



def exit_program():
    print("Goodbye!")
    exit()


def create_agent():
    name = input("Enter Agent's name: ")
    email = input("Enter Agent's email:")
    phone = input("Enter Agent's phone #: ")
    dre_num = int(input("Enter Agent's DRE # : "))
    try:
        agent = Agent.create(name,email,phone,dre_num)
        print(f"Success:{agent}")
    except Exception as e:
        print("Error creating Agent:",e)

# def list_agents():
#     agents = Agent.get_all()
#     for agent in agents:
#         print(f"{agent.id}.{agent.name}")
def manage_agent():
    choice = ""
    while choice !="0":

        print("\n-- Agents Management --\n")
        print("1. List All Agents")
        print("2. Find Agent By Name")
        print("3. Add new Agent")
        print("0. Back to Main Menu")
        choice = input("> ")
        if choice == "1":
            list_agents()
        elif choice == "2":
            find_agent_by_name()
        elif choice == "3":
            create_agent()
        elif choice == "0":
            print(" back to Main Menu")
            return
        else:
            print("Invalid Input!")
            return
# def agent_management_menu():
#     print("\n-- Agents Management --\n")
#     print("1. List All Agents")
#     print("2. Find Agent By Name")
#     print("3. Add new Agent")
#     print("0. Back to Main Menu")

def list_agents():
    agents = Agent.get_all()
    if not agents:
        print("No agents found!")
        return
    else:
        print("\n--- List of Agents ---\n")
        for index, agent in enumerate(agents, start=1):
            print(f"{index}. {agent.name}")
        
        selected_index = int(input("\nEnter the number of the agent to view details or modify (or 0 to go back): \n"))
        
        if 1 <= selected_index <= len(agents):
            selected_agent = agents[selected_index - 1]
            agent_menu(selected_agent)
        elif selected_index == 0:
            return   # Return to the previous menu (Main Menu or Agent Management Menu)
        else:
            print("Invalid selection. Returning to agent management menu.")
            return 

def agent_menu(agent):
    
    print(f"\n--- Managing Agent ---\n\n( Name: {agent.name}, Email: {agent.email}, Phone: {agent.phone}, DRE# : {agent.dre_num})\n")
    print("1. Update Agent")
    print("2. Delete Agent")
    print("3. Add Property for Agent")
    print("4. List Agent's Properties")
    print("0. Back to Agent Management")
    
        # choice = prompt_user("Select an option (1/2/3/4): ", ["1", "2", "3", "4"])
    choice = ""
    while choice !="0":
    
        choice = input("> ")
        if choice == "1":
            update_agent(agent)
        elif choice == "2":
            delete_agent(agent)
        elif choice == "3": 
            add_property_for_agent(agent)
        elif choice == "4":
            list_agent_properties(agent)
        elif choice == "0":
            print("Exitting back to previous menu")
            return  # Go back to the previous menu (Agent Management Menu)
        else:
            print("Invalid Input!")
        
# def find_agent_by_id():
#     id_ = input("Enter Agent's ID : ")
#     if agent:= Agent.find_by_id(id_):
#         # breakpoint()
#         print(agent.name)
#     else:
#         print(f'Agent {id_} not found!')

def find_agent_by_name():
    name = input("Enter Agent's Name: ").title()
    agent = Agent.find_by_name(name)

    if agent:
        print(f"\n--- Agent Found ---")
        print(f"(Name: {agent.name}, Email: {agent.email}, Phone: {agent.phone}, DRE: {agent.dre_num})")
        agent_menu(agent)
    else:
        print(f"Agent '{name} not found. Please chech the name and try again.")
    

def update_agent(agent):
    print(f"\n--- Updating Agent:{agent.name}")

    name = input(f"Enter new name (or press Enter keep {agent.name}):").title() or agent.name
    email = input(f"Enter new email (or press Enter keep {agent.email}):").lower() or agent.email
    phone = input(f"Enter new phone (or press Enter keep {agent.phone}):") or agent.phone
    dre_num = input(f"Enter new DRE# (or press Enter keep {agent.dre_num}):") or agent.dre_num
    confirmation = input(f"Are you sure you want to apply these changes? (Y/N)")

    if confirmation.lower() == "y":
        agent.name = name
        agent.email = email
        agent.phone = phone
        agent.dre_num = dre_num
        agent.update()  
        print(f"\n Agent {agent.name} updated successfully.")
        manage_agent()
    else:
        print("Update canceled.")
        manage_agent()
            

def delete_agent(agent):
    confirmation = input(f"Are you sure you want to delete Agent :{agent.name} ? (Y/N): ").lower()
    if confirmation == "y":
        agent.delete()
        print(f"Agent {agent.name} deleted successfully.")
        manage_agent()
    else:
        print("Deletaion canceled.")
#         manage_agent()
def add_property_for_agent(agent):
    print(f"\n--- Adding Property for Agent: {agent.name} ---")
    address = input("Enter Property Address: ")
    price = int(input("Enter Property price: "))
    confirmation = input(f"Are you sure you want to add this propety for Agent: {agent.name} (Y/N) ? ").lower()
    
    if confirmation =="y":
        property = Property(address,price,agent.id)
        property.save()
        print(f"Property added successfully for Agent {agent.name}.")
        manage_agent()
    else:
        print("Add Property canceled.")

def list_agent_properties(agent):
    properties = Property.get_properties_by_agent(agent.id)
    if not properties:
        print(f"\n{agent.name} has no properties listed.")
        print("\n-- Going back to previous menu.--")
        list_agents()
    else:
        print(f"\n--- Properties for agent: {agent.name} ---")
        for idx,property in enumerate(properties,start=1):
            print(f"{idx}. Address: {property.address}, Price:$ {property.price}.00")
        try:
            selected_index = int(input("\nSelect a property number to View options (or 0 to go back): "))
            if selected_index == 0:
               list_agents()
            elif 1 <=selected_index<=len(properties):
                selected_property = properties[selected_index-1]
                print(f"\n--- Updating Property: {selected_property.address} ---")
                print("1. Update Property \n2. Delete Property \n0. Back to Agent Properties")
                choice = ""
                while choice !="0":
                    choice = input("> ")
                    if choice =="1":
                        address = input(f"Enter new address (or press Enter to keep {selected_property.address}): ") or selected_property.address
                        price = input(f"Enter new price (or Enter to keep {selected_property.price})") or selected_property.price
                        confirmation = input(f"Are you sure you want to update this property? (Y/N): ").lower()
                        if confirmation == "y":
                            selected_property.address = address
                            selected_property.price = price
                            selected_property.update()
                            print(f"Property updated successfully.")
                            list_agent_properties(agent)
                        else:
                            print("Update canceled.")
                            list_agent_properties(agent)
                    elif choice == "2":
                        confirmation = input(f"Are you sure you want to delete the property at {selected_property.address} (Y/N): ?").lower()
                        if confirmation == "y":
                            selected_property.delete()
                            print(f"Property at {selected_property.address} deleted successfully.")
                            return
                        else:
                            print("Deletaion canceled.")
                            list_agent_properties(agent)
                    elif choice == "0":
                        list_agent_properties(agent)
                    else:
                        print("Invalid option.Returning to agent's properties.")
                        list_agent_properties(agent)        
            else:
                print("Invalid selection.Returning to agent menu.")
                # manage_agent()
        except ValueError:
            print("Please enter a valid number.")
            list_agent_properties(agent)

  
    # if agent := Agent.find_by_id(id_):
    #     confirmation = input(f"Are  you sure you want to delet Agent {id_} ({agent.name})? (Y/N): ")
    #     if confirmation.lower() =="y":
    #         agent.delete()
    #         print(f" Agent's {id_} deleted Successfully")
    #     else:
    #         print("Deletaion canceled.")
    # else:
    #     print(f"Agent's id:{id_} not found!")
