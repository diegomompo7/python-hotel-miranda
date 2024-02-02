from ..Model import *
from datetime import *
from ...validators.validators import *


def BookingCreate(newBook, roomId):
        name = input("What's your name: ")
        newBook["name"] = name

        newBook["orderDate"] = date.today().isoformat()

        checkInMessage = "Date to entry (YYYY-MM-DD): "
        check_in = validationDate('check_in', checkInMessage, input(checkInMessage), None)
        newBook["check_in"] = check_in

        hourInMessage = "Time to entry (HH:MM): "
        hour_in = validationTime('hour_in', hourInMessage, input(hourInMessage), None)
        newBook["hour_in"] = hour_in

        checkOutMessage = "Date to out (YYYY-MM-DD): "
        print(newBook)
        check_out = validationDate('check_out', checkOutMessage, input(checkOutMessage), newBook)
        newBook["check_out"] = check_out

        hourOutMessage = "Time to out (HH:MM): "
        hour_out = validationTime('hour_in', hourOutMessage, input(hourOutMessage), None)
        newBook["hour_out"] = hour_out

        roomAvailable = executeQuery(
            "SELECT DISTINCT room_id FROM bookings WHERE room_id NOT IN (SELECT DISTINCT room_id FROM bookings WHERE (check_in < %s AND check_out > %s));",
            (f"'{check_out}'", f"'{check_in}'"),
            "GET",
        )
        
        print(roomAvailable)

        for i in range(0, len(roomAvailable)):
            roomId.append(roomAvailable[i]["room_id"])

        chooseRoomMessage = f"Choose a room {roomId}: "
        checkRoom = validationOption("room_id", chooseRoomMessage, None, roomId)
        newBook["room_id"] = checkRoom

        specialRequest = input("Enter a special request (OPTIONAL): ")
        checkSpecialRequest = validationExists(
            "specialRequest", specialRequest, None
        )
        newBook["specialRequest"] = checkSpecialRequest

        newBook["status"] = "Check In"
        
        return newBook