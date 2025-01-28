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

def list_agents():
    agents = Agent.get_all()
    for agent in agents:
        print(agent)
        
def find_agent_by_id():
    id_ = input("Enter Agent's ID : ")
    if agent:= Agent.find_by_id(id_):
        print(agent)
    else:
        print(f'Agent {id_} not found!')

def find_by_name():
    name = input("Enter Agent's Name: ")
    if agent:= Agent.find_by_name(name):
        print(agent)
    else:
        print(f"Agent {name} not found!")

def update_agent():
    id_ = input("Enter Agent's ID : ")
    if agent := Agent.find_by_id(id_):
        try:
            name = input("Enter Agent's new name: ")
            if name:
                agent.name = name
            email = input("Enter Agent's new email :")
            if email:
                agent.email = email
            phone = input("Enter Agen's new phone # :")
            if phone:
                agent.phone = phone
            dre_num = (input("Enter Agent's DRE # :"))
            if dre_num:
                agent.dre_num = int(dre_num)
            agent.update()  
            print(f" Success : {agent}")
        except Exception as e:
            print(f"Error Updating Agent",{e})
    else:
        print(f"Agent: {id_} not found!")

def delete_agent():
    id_ = input("Enter Agent's ID:")
    if agent := Agent.find_by_id(id_):
        agent.delete()
        print(f" Agent {id_} Deleted:")
    else:
        print(f"Agent's id:{id_} not found!")