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