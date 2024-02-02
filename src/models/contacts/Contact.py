from ..Model import *
from .ContactCreate import ContactCreate
from .ContactUpdate import ContactUpdate


class Contacts(Model):
    table = "contacts"

    def __init__(self, id):
        self.id = id

    @classmethod
    def create(cls):
        newContact = {}
        fields = executeQuery("SHOW FIELDS FROM %s", Contacts.table, "GET")
        for i in range(1, len(fields)):
            newContact[fields[i]["Field"]] = ""
        
        super(Contacts, cls).create(cls.table, ContactCreate(newContact))

    @classmethod
    def update(cls, id):
        contact_data = Contacts.view(str(id))
        updateContact = contact_data

        super(Contacts, cls).update(cls.table, ContactUpdate(contact_data, updateContact, id))
