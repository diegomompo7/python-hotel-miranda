from ..Model import *
from datetime import *
from ...validators.validators import *


def BookingCreate(newBook, roomId):
        name = input("What's your name: ")
        newBook["name"] = name

        newBook["orderDate"] = date.today().isoformat()

        checkInMessage = "Date to entry (YYYY-MM-DD): "
        check_in = validationDate('check_in', checkInMessage, None)
        newBook["check_in"] = check_in

        hour_in = input("Date to entry (HH:MM): ")
        newBook["hour_in"] = hour_in

        checkOutMessage = "Date to out(YYYY-MM-DD): "
        print(newBook)
        check_out = validationDate('check_out', checkOutMessage, newBook)
        newBook["check_out"] = check_out

        hour_out = input("Date to out (HH:MM): ")
        newBook["hour_out"] = hour_out

        roomAvailable = executeQuery(
            "SELECT room_id FROM bookings WHERE check_in > %s OR check_out < %s;",
            (f"'{check_out}'", f"'{check_in}'"),
            "GET",
        )

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