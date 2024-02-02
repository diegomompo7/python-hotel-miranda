from ..Model import *

from .UserCreate import UserCreate
from .UserUpdate import UserUpdate



class Users(Model):
    table = "users"

    def __init__(self, id, table):
        self.id = id
        self.table = table
        
    @classmethod   
    def create(cls):
        newUser = {}
        fields = executeQuery("SHOW FIELDS FROM %s", Users.table, "GET")
        for i in range(1, len(fields)):
            newUser[fields[i]["Field"]] = ""

        super(Users, cls).create(cls.table, UserCreate(newUser))

    @classmethod  
    def update(cls, id):
        user_data = Users.view(str(id))
        updateUser = user_data

        super(Users, cls).update(cls.table, UserUpdate(user_data, updateUser))
