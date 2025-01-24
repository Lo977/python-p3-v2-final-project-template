from models.__init__ import CONN,CURSOR



class Agent:
    all = []
    def __init__(self,name,email,phone,dre_num=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.dre_num = dre_num
        Agent.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name,str) and len(name) > 0:
            self._name = name
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,email):
        if len(email) > 0:
            self._email = email