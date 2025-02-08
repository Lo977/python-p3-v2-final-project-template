from models.__init__ import CURSOR,CONN
from models.property import Property


class Agent:
    all = {}
    def __init__(self, name, email, phone, dre_num,id=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.dre_num = dre_num
        

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name,str) and len(name) > 0 :
            self._name = name.title()
        else:
            raise ValueError("Name must be non_empty strings ")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABlE IF NOT EXISTS agents (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            phone INTEGER,
            dre_num INTEGER)
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql ="DROP TABLE IF EXISTS agents"

        CURSOR.execute(sql)
        CONN.commit()


    def save(self):
        sql = """
            INSERT INTO agents(name, email, phone, dre_num)
            VALUES (?, ?, ?, ?) 
         """
        CURSOR.execute(sql,(self.name, self.email, self.phone, self.dre_num))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self


    @classmethod
    def create(cls, name, email, phone, dre_num):
        agent = cls(name, email, phone, dre_num)    
        agent.save()
        return agent
    
    @classmethod
    def instance_from_db(cls,row):
        agent = cls.all.get(row[0])
        if agent:
            agent.name = row[1]
            agent.email = row[2]
            agent.phone = row[3]
            agent.dre_num  = row[4]
        else:
            agent = cls(row[1],row[2],row[3],row[4])
            agent.id = row[0]
            cls.all[agent.id] = agent
        return agent
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM agents"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def update(self):
        sql = """
            UPDATE agents 
            SET name = ?, email = ?, phone = ?, dre_num = ?
            WHERE id = ?
        """
        CURSOR.execute(sql,(self.name, self.email, self.phone, self.dre_num, self.id))
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
    def find_by_name(cls,name):
        sql = """
            SELECT *
            FROM agents
            WHERE name = ?
        """
        row = CURSOR.execute(sql,(name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def properties(self):
       return Property.get_properties_by_agent(self.id)

