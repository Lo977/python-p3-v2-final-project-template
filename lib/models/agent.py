# lib/models/agent.py
from models.__init__ import CURSOR, CONN
import re



class Agent:
    all = {}
    def __init__(self,name,email, phone, dre_num, id=None):
        # print(f"Creating agent: name={name}, email={email}, phone={phone}, dre_num={dre_num}")
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.dre_num = dre_num
        
    # def __repr__(self):
    #     return f"<Agent {self.id} Name: {self.name} Email: {self.email} Phone: {self.phone} Dre_num: {self.dre_num}>"
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name,str) and len(name) > 0:
            self._name = name.title()
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
            email TEXT ,
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
        existing_agent = cls.duplicate_check_point(email,phone,dre_num)
        if existing_agent:
            print(f"Agent already exists:{existing_agent}")
        else:
            agent =cls(name, email, phone, dre_num)
            agent.save()    
            return agent
        
    def update(self):
        sql = """
            UPDATE agents 
            SET name = ?,email = ?,phone = ?,dre_num = ?
            WHERE id = ?
       """
        CURSOR.execute(sql,(self.name,self.email,self.phone,self.dre_num,self.id))
        CONN.commit()
    def delete(self):
        sql = """
            DELETE FROM agents
            WHERE id = ? 
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls,row):
        # print(f"Debug: row fetched from database: {row}")
        agent = cls.all.get(row[0]) 
        if agent:
            agent.name = row[1]
            agent.email = row[2]
            agent.phone = row[3]
            agent.dre_num = row[4]
            # print(agent)
        else:
            agent = cls(row[1],row[2],row[3],row[4])
            agent.id = row[0]
            cls.all[agent.id] = agent
            # print(f"Debug: agent created: {agent}")
        return agent
    # 2
    # 2 cls.instance_from_db(row) if row else None
    @classmethod
    def duplicate_check_point(cls,email,phone,dre_num):
        sql ="""
            SELECT *
            FROM agents
            WHERE email = ? OR phone = ? OR dre_num = ?
        """
        row = CURSOR.execute(sql,(email,phone,dre_num)).fetchone()
        return cls.instance_from_db(row) if row else None
        
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM agents
        """
        rows = CURSOR.execute(sql).fetchall()   
        # print(f"Debug: all rows fetched: {rows}")
        return[cls.instance_from_db(row) for row in rows]
    @classmethod
    def find_by_id(cls,id):
        sql = """
            SELECT *
            FROM agents
            WHERE id = ?
        """
        row = CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def find_by_name(cls,name):
        sql = """
            SELECT *
            FROM  agents
            WHERE name = ?
        """
        row = CURSOR.execute(sql,(name,)).fetchone()
        return cls.instance_from_db(row) if row else None

# print(Agent.all)

# agent1 = Agent.create("Rakesh","rakesh@emal.com","444-423-2345",123445)
# agent2 = Agent.create("James","james@emal.com","422-423-2322",232985)
# agent1 = Agent.create("Hanry","henty@emal.com","267-324-8732",782738)
# agent1 = Agent.create("Katie","katie@emal.com","098-789-7244",478639)
# agent1 = Agent.create("Adam","adam@emal.com","778-563-2451",728394)
# agent1.dre_num = "00000000"
# # 
# print(agent1.dre_num)
# agent1 = Agent("avb","afv@g.com","222-333-4444",123456)