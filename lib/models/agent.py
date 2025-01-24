from models.__init__ import CONN,CURSOR



class Agent:
    all = []
    def __init__(self,name,email,phone,dre_num=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.dre_num = dre_num
        Agent.all.append(self)