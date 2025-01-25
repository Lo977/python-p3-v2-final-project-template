from models.__init__ import CURSOR,CONN
from models.agent import Agent
import re


class Property:
    all ={}
    def __init__(self, address,price,size,bedroom,description,agent_id,id=None):
        self.id = id
        self.address = address
        self.price = price
        self.size = size
        self.bedroom = bedroom
        self.description = description
        self.agent_id = agent_id
        # Property.all.append(self)
# , price, size, bedroom, description, agent
    def __repr__(self): 
        return f"(<Address : {self.address} \n Price : ${self.price}\n Size: {self.size} SQ FT\n Bedroom: {self.bedroom}\n Description : {self.description}>)"
    
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        
        address_regex = r"^\d{1,5}\s[a-zA-Z0-9\s]{1,}\,?\s[a-zA-Z\s]+(?:\s(?:Apt|Suite|Unit)\s?\d{1,5}[A-Za-z]?)?,?\s[a-zA-Z\s]+\,\s[A-Z]{2}\s\d{5}(-\d{4})?$"
        
        if re.match(address_regex, address) and len(address) != 0:
            self._address = address  
        else:
            raise ValueError("Invalid address format!")

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,price):
        if isinstance(price,(int,float)) and price > 0:
            self._price = price
        else:
            raise ValueError("Price must be a positve numbers.")
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,size):
        if isinstance(size,(int,float)) and size > 0:
            self._size = size
        else:
            raise ValueError("Size must be non-empty numbers")
    @property
    def bedroom(self):
        return self._bedroom
    @bedroom.setter
    def bedroom(self,bedroom):
        if isinstance(bedroom,int) and bedroom >=1:
            self._bedroom = bedroom
        else:
            raise Exception("Invalid Bedroom Numbers.")
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self,description):
        if isinstance(description,str):
            self._description = description 
        else:
            raise ValueError("Desciption must be non-empty strings.")
    @property
    def agent_id(self):
        return self._agent_id
    @agent_id.setter
    def agent_id(self,agent_id):
        if isinstance(agent_id,int) and Agent.find_by_id(agent_id):
            self._agent_id = agent_id
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS properties (
            id INTEGER PRIMARY KEY,
            address TEXT,
            price INTEGER,
            size INTEGER,
            bedroom INTEGER,
            description TEXT,
            agent_id INTEGER,
            FOREIGN KEY(agent_id)REFERENCES agents(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS properties
        """
        CURSOR.execute(sql)
        CONN.commit()




# property1 = Property("123 Market St, san francisco, CA 12344",2353535,2000,5,"beutifull stunnig.")
# print(Property.all)