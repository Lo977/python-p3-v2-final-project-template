#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.agent import Agent
from models.property import Property
import ipdb

def reset_database():
    Property.drop_table()
    Agent.drop_table()
    Agent.create_table()
    Property.create_table() 


try:
    reset_database()
except Exception as e:
    print(f"Error during database reset: {e}")

ipdb.set_trace()


