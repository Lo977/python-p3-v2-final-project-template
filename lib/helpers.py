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
        for index,agent in enumerate(agents,start=1):
            print(f"{index}.{agent.name}")
    try:
        selected_inex = int(input("Enter the number of the agent you want to select:"))
        if 1 <= selected_inex <= len(agents):
            selected_agent = agents[selected_inex - 1]   
            print(f"name: {selected_agent.name}, email: {selected_agent.email} phone: {selected_agent.phone} Dre #:{selected_agent.dre_num}")
        else:
            print("Invalid index! Please enter a valid number from the list.")
    except ValueError:
        print("Please enter a valid number.")

        
def find_agent_by_id():
    id_ = input("Enter Agent's ID : ")
    if agent:= Agent.find_by_id(id_):
        print(agent)
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
