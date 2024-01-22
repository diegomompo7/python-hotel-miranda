from models.models import *
from models.bookings import Bookings
import argparse

    
def bookings():
    type = input("Insert the type of select (list, view, create, udpate, delete): ")
    
    actionBooking= {
        "list": Bookings.list,
        "view": Bookings.view,
        "create": Bookings.create,
        "update": Bookings.update, 
        "delete": Bookings.delete, 
    }
    
    if type or actionBooking:
        if type=="list" or type=="create":
            actionBooking[type]()
        else: 
            id = input("Insert the id of booking: ")
            actionBooking[type](id)
    else:
        print(f"{type} is not a type of select")
    
def list_rooms():
    Rooms.list()

def list_contacts():
    Contact.list()

def list_users():
    Users.list()
    
def main():
    parser = argparse.ArgumentParser(description="app reads bookings, rooms, contacts and users")
    parser.add_argument('action', help="Action to realise")
    
    
    args = parser.parse_args()
    
    actions = {
        "bookings": bookings,
        "list-rooms": list_rooms,
        "list-contacts": list_contacts,
        "list-users": list_users,
    }
    
    if args.action in actions:
        actions[args.action]()
    else:
        print(f'Can not find function {args.action}')
        
if __name__ == '__main__':
    main()