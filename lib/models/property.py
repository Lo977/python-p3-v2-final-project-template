from models.__init__ import CURSOR,CONN
from models.agent import Agent


class Property:

    all = {}

    def __init__(self, address, price, agent_id):
        self.id = id
        self.address = address
        self.price = price
        self.agent_id = agent_id

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
        sql = "DROP TABLE IF EXISTS properties"

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO properties (address,price,agent_id)
            VALUES(?, ?, ?)
        """
        CURSOR.execute(sql,(self.address, self.price, self.agent_id))
        CONN.commit()   

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self