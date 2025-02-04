
from models.agent import Agent
from models.property import Property


def exit_program():
    exit()

def create_agent(name,email,phone,dre_num):
    return Agent.create(name, email, phone, dre_num)

def get_all_agents():
    return Agent.get_all()

def update_agent(agent):
    agent.update()

def delete_agent(agent):
    agent.delete()

def find_agent_by_name():
    name = input(f"Enter Agent's name: ").title()
    agent = Agent.find_by_name(name)

    if agent:
        print(f"\n-- Agent found --")
        print(f"\n Name: {agent.name}, Email: {agent.email}, Phone: {agent.phone}, DRE #: {agent.dre_num} ")
    else:
         print(f"❌ Agent '{name}' not found.")

def add_property(address,price,agent):
    property = Property(address, price, agent.id)   
    property.save()