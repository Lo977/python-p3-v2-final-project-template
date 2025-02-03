from models.__init__ import CURSOR,CONN

class Agent:
    all = {}
    def __init__(self, name, email, phone, dre_num):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.dre_num = dre_num
        pass

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