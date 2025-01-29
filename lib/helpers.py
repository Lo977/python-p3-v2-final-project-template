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
def list_agents():
    agents = Agent.get_all()
    if not agents:
        print("No agents found!")
        return
    else:
        print("\n--- List of Agents ---")
        for index, agent in enumerate(agents, start=1):
            print(f"{index}. {agent.name}")
        
        selected_index = int(input("\n Enter the number of the agent you want to select (or 0 to go back): "))
        
        if 1 <= selected_index <= len(agents):
            selected_agent = agents[selected_index - 1]
            agent_menu(selected_agent)
        elif selected_index == 0:
            return  # Return to the previous menu (Main Menu or Agent Management Menu)
        else:
            print("Invalid selection. Returning to agent management menu.")
            return

def agent_menu(agent):
    
    print(f"\n--- Managing Agent: {agent.name} ---")
    print("1. Update Agent")
    print("2. Delete Agent")
    print("3. Add Property for Agent")
    print("0. Back to Agent Management")
    
        # choice = prompt_user("Select an option (1/2/3/4): ", ["1", "2", "3", "4"])
    choice = ""
    while choice !="0":
    
        choice = input("> ")
        if choice == "1":
            pass
            # update_agent(agent)
        elif choice == "2":
            pass
            # delete_agent(agent)
        elif choice == "3":
            pass
            # add_property_for_agent(agent)
            pass
        elif choice == "0":
            print("Exitting back to previous menu")
            return  # Go back to the previous menu (Agent Management Menu)
        else:
            print("Invalid Input!")
        
def find_agent_by_id():
    id_ = input("Enter Agent's ID : ")
    if agent:= Agent.find_by_id(id_):
        # breakpoint()
        print(agent.name)
    else:
        print(f'Agent {id_} not found!')

def find_by_name():
    name = input("Enter Agent's Name: ")
    name = name.title()
    if agent:= Agent.find_by_name(name):
        print(agent)
    else:
        print(f"Agent {name} not found!")

def update_agent():
    id_ = input("Enter Agent's ID : ")
    if agent := Agent.find_by_id(id_):
        try:
            name = input("Enter new name (or press Enter keep the current value):")
            name = name if name else agent.name

            email = input("Enter new email (or press Enter keep the current value):")
            email = email if email else agent.email

            phone = input("Enter new phone (or press Enter keep the current value):")
            phone = phone if phone else agent.phone

            dre_num = input("Enter new DRE# (or press Enter keep the current value):")
            dre_num =  int(dre_num) if dre_num else agent.dre_num

            confirmation = input(f"Are you sure you want to apply these changes? (Y/N):")
            if confirmation.lower() == "y":
                agent.name = name
                agent.email = email
                agent.phone = phone
                agent.dre_num = dre_num
                agent.update()  
                print(f" Agent {id_} updated successfully.")
            else:
                print("Update canceled.")
        except Exception as e:
            print(f"Error Updating Agent",{e})
    else:
        print(f"Agent: {id_} not found!")

def delete_agent():
    id_ = input("Enter Agent's ID:")
    if agent := Agent.find_by_id(id_):
        confirmation = input(f"Are  you sure you want to delet Agent {id_} ({agent.name})? (Y/N): ")
        if confirmation.lower() =="y":
            agent.delete()
            print(f" Agent's {id_} deleted Successfully")
        else:
            print("Deletaion canceled.")
    else:
        print(f"Agent's id:{id_} not found!")
