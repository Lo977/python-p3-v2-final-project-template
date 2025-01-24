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
    
    @property
    def phone(self):
        return self._phone
    @phone.setter
    def phone(self,phone):
        if isinstance(phone,int) and len(phone) > 10:
            self._phone = phone
    @property
    def dre_num(self):
        return self._dre_num
    @dre_num.setter
    def dre_num(self,dre_num):
        if isinstance(dre_num,int) and len(dre_num) > 6:
            self._dre_num = dre_num