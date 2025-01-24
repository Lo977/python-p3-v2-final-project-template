from models.__init__ import CURSOR,CONN
from models.agent import Agent


class Property:
    all =[]
    def __init__(self,address, price, size, bedroom, description, agent):
        self.address = address
        self.price = price
        self.size = size
        self.bedroom = bedroom
        self.description = description
        self.agent = agent
        Property.all.append(self)

    @property
    def address(self):
        return self._address
    @address.setter
    def address(self,address):
        if isinstance(address,str) and len(address) > 5:
            self._address = address
        else:
            raise ValueError("Address must be non-empty string")

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,price):
        if isinstance(price,float) and price > 0:
            self._price = price
        else:
            raise ValueError("Price must be non-empty numbers")
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,size):
        if isinstance(size,int) and size > 0:
            self._size = size
        else:
            raise ValueError("Size must be non-empty numbers")
        