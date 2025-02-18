
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

def list_properties(agent):
    # breakpoint()
    # properties = Property.get_properties_by_agent(agent.id) 
    properties = agent.properties()
    if not properties:
        print(f"\n-- Agent: {agent.name} has no property listed. --")
        return
    
    print(f"\n-- Prperties for Agent: {agent.name}")

    for i,property in enumerate(properties, start=1):
        print(f"\n{i}. Address: {property.address}, Price: $ {property.price}.00")
  
    while True:
        try:
           
            selected_index = int(input("\n-- Select property number for options (or 0 to go back): "))
            if selected_index == 0:
                print("\nNavigating back to previous menu.")
                return
            elif 1 <= selected_index <= len(properties):
                property_options(properties[selected_index-1])
            else:
                print("Invalid selection. Try again")
        except ValueError:
            print("Please enter a valid number.")

def property_options(property):
    choice = ""
    while choice != "0":
        print(f"\n Property: {property.address} \n")
        print(f"Manage Property\n")
        print("1. Update Property")
        print("2. Delete Property")
        print("0. Back to previous Menu")

        choice = input("> ").strip()    
        if choice =="1":
            update_property(property)
        elif choice == "2":
            delete_property(property)
        elif choice != "0":
            print("\n-- Invalid selection.Try again --")
    print(f"\n-- Navigating back to previous menu --")

def update_property(property):
    address = input(f"Enter new address (or press Enter to keep {property.address}) ") or property.address
    price = input(f"Enter new price (or press Enter to keep {property.price})")

    confirmation = input("Are you sure you an to update this property? (Y/N): ")
    if confirmation == "y":
        property.address = address
        property.price = int(price) if price else property.price
        property.update()
        print("\n✅ Property updated successfully. ")
    else:
        print("\n❌ Property update canceled.")

def delete_property(property):
    confirmaion = input(f"\n Are you sure you want to Delete property: {property.address} ? (Y/N): ").lower()

    if confirmaion == "y":
        property.delete()
        print("\n✅ Property deleted successfully.")
        return True
    else:
         print("\n❌ Property deletion canceled.")