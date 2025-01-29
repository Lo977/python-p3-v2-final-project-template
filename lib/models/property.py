from models.__init__ import CURSOR,CONN
from models.agent import Agent
import re


class Property:
    all ={}
    def __init__(self, address,price,agent_id,id=None):
        self.id = id
        self.address = address
        self.price = price
        self.agent_id = agent_id
        
    def __repr__(self): 
        return f"(<Address : {self.address} \n Price : ${self.price}>)"
    
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        
        # address_regex = r"^\d{1,5}\s[a-zA-Z0-9\s]{1,}\,?\s[a-zA-Z\s]+(?:\s(?:Apt|Suite|Unit)\s?\d{1,5}[A-Za-z]?)?,?\s[a-zA-Z\s]+\,\s[A-Z]{2}\s\d{5}(-\d{4})?$"
        
        if isinstance(address,str) and len(address) != 0:
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
    def save(self):
        sql ="""
            INSERT INTO properties (address,price,agent_id)
            VALUES(?,?,?)
        """
        CURSOR.execute(sql,(self.address,self.price,self.agent_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def instance_from_db(cls, row):
        property_instance = cls(
            address=row[1],    
            price=row[2],       
            agent_id=row[3],   
            id=row[0]          
        )
        return property_instance
    
    @classmethod
    def get_properties_by_agent(cls,agent_id):
        sql = """
            SELECT *
            FROM properties
            WHERE agent_id = ?
        """
        rows = CURSOR.execute(sql,(agent_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    def update(self):
        sql = """
            UPDATE properties
            SET address =?, price =?
            WHERE agent_id =?
        """
        CURSOR.execute(sql,(self.address,self.price,self.agent_id))
        CONN.commit()




# property1 = Property("123 Market St, san francisco, CA 12344",2353535,2000,5,"beutifull stunnig.")