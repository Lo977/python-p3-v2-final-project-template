
from models.agent import Agent


def exit_program():
    exit()

def create_agent(name,email,phone,dre_num):
    return Agent.create(name, email, phone, dre_num)

def get_all_agents():
    return Agent.get_all()