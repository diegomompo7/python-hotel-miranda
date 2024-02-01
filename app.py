from src.models.bookings import Bookings
from src.models.rooms import Rooms
from src.models.contacts import Contacts
from src.models.users import Users
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="app select bookings, rooms, contacts and users"
    )
    parser.add_argument("table", help="Table to select")
    parser.add_argument("action", help="Action to realise")
    parser.add_argument("id", nargs='?', help="Action to realise")

    args = parser.parse_args()

    actions = {
        "bookings": {
            "list": Bookings.list,
            "view": Bookings.view,
            "create": Bookings.create,
            "update": Bookings.update,
            "delete": Bookings.delete,
        },
        "rooms": {
            "list": Rooms.list,
            "view": Rooms.view,
            "create": Rooms.create,
            "update": Rooms.update,
            "delete": Rooms.delete,
        },
        "contacts": {
            "list": Contacts.list,
            "view": Contacts.view,
            "create": Contacts.create,
            "update": Contacts.update,
            "delete": Contacts.delete,
        },
        "users": {
            "list": Users.list,
            "view": Users.view,
            "create": Users.create,
            "update": Users.update,
            "delete": Users.delete,
    },
    }

    if args.table in actions and args.action in actions[args.table]:
        
        if args.id:
            print(args.id)
            actions[args.table][args.action](args.id)
        else:
            actions[args.table][args.action]()
    else:
        print(f"Cannot find function {args.action} in {args.table}")


if __name__ == "__main__":
    main()
