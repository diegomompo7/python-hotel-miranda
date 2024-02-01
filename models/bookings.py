from models.models import *
from models.rooms import Rooms
from datetime import *


class Bookings(Model):
    table = "bookings"

    def __init__(self, id, table):
        self.id = id
        self.table = table

    def create():

        roomId=[]
        newBook = {}
        fields = executeQuery("SHOW FIELDS FROM %s", Bookings.table, "GET")
        for i in range(1, len(fields)):
            newBook[fields[i]["Field"]] = ""
        
        name = input("What's your name: ")
        newBook['name'] = name
        
        newBook['orderDate'] = date.today().isoformat()
        
        check_in = input("Date to entry (YYYY-MM-DD): ")
        newBook['check_in'] = check_in
        
        hour_in = input("Date to entry (HH:MM): ")
        newBook['hour_in'] = hour_in
        
        check_out = input("Date to out(YYYY-MM-DD): ")
        newBook['check_out'] = check_out
        
        hour_out = input("Date to out (HH:MM): ")
        newBook['hour_out'] = hour_out

        roomAvailable = executeQuery("SELECT room_id FROM bookings WHERE check_in > %s OR check_out < %s;", (f'\'{check_out}\'', f'\'{check_in}\''), "GET")
        
        for i in range (0, len(roomAvailable)):
            roomId.append(roomAvailable[i]['room_id'])
        
        chooseRoomMessage = f"Choose a room {roomId}: "
        checkRoom = Model.validationOption("room_id", chooseRoomMessage, None, roomId)
        newBook["room_id"] = checkRoom
        
        
        specialRequest = input("Enter a special request (OPTIONAL): ")
        checkSpecialRequest = Model.validationEmpty("specialRequest", specialRequest, None)
        newBook['specialRequest'] = checkSpecialRequest
        
        newBook['status'] = "Check In"

        Model.create(Bookings.table, newBook)

    def update(id):
        roomId = []
        booking_data = Bookings.view(str(id))
        updateBook = booking_data
        statusBooking = ["Check In", "Check Out", "In Progress"]

        name = input(f"What's your name (default {updateBook['name']}): ")
        updateBook["name"] = Model.validationEmpty("name", name, booking_data)

        check_in = input(f"Date to entry (YYYY-MM-DD) (default {updateBook['check_in']}): ")
        updateBook["check_in"] = Model.validationEmpty("check_in", check_in, booking_data)
        
        hour_in = input(f"Date to entry (HH:MM)  (default {updateBook['hour_in']}): ")
        updateBook["hour_in"] = Model.validationEmpty("hour_in", hour_in, booking_data)
        
        check_out = input(f"Date to entry (YYYY-MM-DD)  (default {updateBook['check_out']}): ")
        updateBook["check_out"] = Model.validationEmpty("check_out", check_out, booking_data)
        
        hour_out = input(f"Date to entry (HH:MM) (default {updateBook['hour_out']}): ")
        updateBook["hour_out"] = Model.validationEmpty("hour_out", hour_out, booking_data)
        
 
        roomAvailable = executeQuery("SELECT room_id FROM bookings WHERE check_in > %s OR check_out < %s;", (f'\'{updateBook["check_out"]}\'', f'\'{updateBook["check_in"]}\''), "GET")
        
        for i in range (0, len(roomAvailable)):
            roomId.append(roomAvailable[i]['room_id'])
        
        chooseRoomMessage = f"Choose a room {roomId} (defualt {booking_data['room_id']}): "
        checkRoom = Model.validationOption("room_id", chooseRoomMessage, booking_data, roomId)
        updateBook["room_id"] = checkRoom

        specialRequest = input(f"Enter a special request (OPTIONAL) (default {updateBook['specialRequest']}): ")
        updateBook['specialRequest'] = Model.validationEmpty("specialRequest", specialRequest, booking_data)

        statusMessage = (f"Enter a status {statusBooking} (default {booking_data['status']}): ")
        status = Model.validationOption("status", statusMessage, booking_data, statusBooking)
        updateBook["status"] = status

        Model.update(Bookings.table, updateBook, id)
