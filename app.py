from models.bookings import Bookings
from models.rooms import Rooms
from models.contacts import Contacts
from models.users import Users
from models.models import *
import argparse

    
def bookings():
    type = input("Insert the type of select (list, view, create, udpate, delete): ")
    
    actionBooking = {
        "list": list,
        "view": Bookings.view,
        "create": Bookings.create,
        "update": Bookings.update, 
        "delete": Bookings.delete, 
    }
    
    if type in actionBooking:
        if type=="list" or type =="create":
            print(actionBooking[type])
            actionBooking[type]()
        else: 
            id = input("Insert the id of booking: ")
            actionBooking[type](id)
    else:
        print(f"{type} is not a type of select")
    

def rooms():
    type = input("Insert the type of select (list, view, create, update, delete): ")
    
    actionRoom = {
        "list": Rooms.list,
        "view": Rooms.view,
        "create": Rooms.create,
        "update": Rooms.update, 
        "delete": Rooms.delete, 
    }
    
    if type in actionRoom:
        if type=="list" or type =="create":
            actionRoom[type]()
        else: 
            id = input("Insert the id of room: ")
            actionRoom[type](id)
    else:
        print(f"{type} is not a type of select")

def contacts():
    type = input("Insert the type of select (list, view, create, update, delete): ")
    
    actionContact = {
        "list": Contacts.list,
        "view": Contacts.view,
        "create": Contacts.create,
        "update": Contacts.update, 
        "delete": Contacts.delete, 
    }
    
    if type in actionContact:
        if type=="list" or type =="create":
            actionContact[type]()
        else: 
            id = input("Insert the id of contact: ")
            actionContact[type](id)
    else:
        print(f"{type} is not a type of select")

def users():
    type = input("Insert the type of select (list, view, create, update, delete): ")
    
    actionUser = {
        "list": Users.list,
        "view": Users.view,
        "create": Users.create,
        "update": Users.update, 
        "delete": Users.delete, 
    }
    
    if type in actionUser:
        if type=="list" or type =="create":
            actionUser[type]()
        else: 
            id = input("Insert the id of contact: ")
            actionUser[type](id)
    else:
        print(f"{type} is not a type of select")

    
def main():
    parser = argparse.ArgumentParser(description="app select bookings, rooms, contacts and users")
    parser.add_argument('action', help="Action to realise")
    
    
    args = parser.parse_args()
    
    actions = {
        "bookings": bookings,
        "rooms": rooms,
        "contacts": contacts,
        "users": users,
    }
    
    if args.action in actions:
        actions[args.action]()
    else:
        print(f'Can not find function {args.action}')
        
if __name__ == '__main__':
    main()