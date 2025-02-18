from models.__init__ import CURSOR,CONN

class Property:

    all = {}

    def __init__(self, address, price, agent_id,id=None):
        self.id = id
        self.address = address
        self.price = price
        self.agent_id = agent_id
   
    @property
    def address(self):
        return self._address
    @address.setter
    def address(self,address):
        if isinstance(address,str) and len(address):
            self._address = address   
        else:
            raise ValueError("address must be  non-empty string .")
    
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,price):
        if isinstance(price,(int,float)) and price > 0 :
            self._price = price
        else:
            raise ValueError("Price must be in numbers and greater then 0")

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
    @classmethod
    def instance_from_db(cls, row):
        if not row:  # Ensure row exists
            return None
        property = cls.all.get(row[0])

        if property:
            property.address = row[1]
            property.price = row[2]
            property.agent_id = row[3]
        else:
            property = cls(row[1],row[2],row[3]) 
            property.id = row[0]
            cls.all[property.id] = property
        return property

    def save(self):
       
        sql = "SELECT * FROM properties WHERE address = ?"
        CURSOR.execute(sql,(self.address,))
        
        existing_property = CURSOR.fetchone()
        if existing_property:
            raise ValueError("\n❌ A property with this address already exists.")
        
        sql = """
            INSERT INTO properties (address,price,agent_id)
            VALUES(?, ?, ?)
        """
        CURSOR.execute(sql,(self.address, self.price, self.agent_id))
        CONN.commit()   

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):
        sql = """
            UPDATE properties
            SET address = ?, price = ?
            WHERE id = ?
        """
        CURSOR.execute(sql,(self.address,self.price,self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM properties
            WHERE id = ?
        """
        CURSOR.execute(sql,(self.id,)) 
        CONN.commit()

        if self.id in Property.all:
            del Property.all[self.id]
            self.id = None