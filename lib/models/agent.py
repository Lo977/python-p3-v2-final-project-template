# lib/models/agent.py
from models.__init__ import CURSOR, CONN
import re



class Agent:
    all = {}
    def __init__(self,name,email,phone,dre_num,id = None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.dre_num = dre_num

        # Agent.all.append(self)
    def __repr__(self):
        return f"<Agent {self.id} Name: {self.name} Email: {self.email} Phone: {self.email} Dre_num: {self.dre_num}>"
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name,str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be non-empty strings")

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,email):
        email_re = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.match(email_re,email) and len(email) > 0:
            self._email = email
        else:
            raise ValueError("Email must be in 'email@example.com' !")
    
    @property
    def phone(self):
        return self._phone
    @phone.setter
    def phone(self,phone):
        phone_regex = r"^\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}$"
        if re.match(phone_regex,phone) and len(phone) > 10:
            self._phone = phone
        else:
            raise ValueError("Invalid numbers")
    @property
    def dre_num(self):
        return self._dre_num
    @dre_num.setter
    def dre_num(self,dre_num):
        if isinstance(dre_num,int) and dre_num >= 6:
            self._dre_num = dre_num
        else:
            raise ValueError("Invalid Dre, Numbers!!!")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS agents (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            phone TEXT,
            dre_num INTEGER)
        """   
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS agents        """
        CURSOR.execute(sql)
        CONN.commit()
    def save(self):
        sql = """
            INSERT INTO agents (name,email,phone,dre_num)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql,(self.name, self.email, self.phone, self.dre_num))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls,name,email,phone,dre_num):
        agent =cls(name,email,phone,dre_num)
        agent.save()    
        return agent

# print(Agent.all)

agent1 = Agent("Rakesh","rakesh@emal.com","444-423-2345",123445)
# agent1.dre_num = "00000000"
# # 
# print(agent1.dre_num)
# agent1 = Agent("avb","afv@g.com","222-333-4444",123456)