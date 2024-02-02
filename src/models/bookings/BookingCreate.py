from ..Model import *
from datetime import *
from ...validators.validators import *


def BookingCreate(newBook, roomId):
        nameInput = "What's your name: "
        newBook["name"] = validationEmpty(nameInput, input(nameInput))

        newBook["orderDate"] = date.today().isoformat()

        checkInInput = "Date to entry (YYYY-MM-DD): "
        check_in = validationDate('check_in', checkInInput, input(checkInInput), None)
        newBook["check_in"] = check_in

        hourInInput = "Time to entry (HH:MM): "
        hour_in = validationTime('hour_in', hourInInput, input(hourInInput), None)
        newBook["hour_in"] = hour_in

        checkOutInput = "Date to out (YYYY-MM-DD): "
        check_out = validationDate('check_out', checkOutInput, input(checkOutInput), newBook)
        newBook["check_out"] = check_out

        hourOutInput = "Time to out (HH:MM): "
        hour_out = validationTime('hour_in', hourOutInput, input(hourOutInput), None)
        newBook["hour_out"] = hour_out

        roomAvailable = executeQuery(
            "SELECT DISTINCT room_id FROM bookings WHERE room_id NOT IN (SELECT DISTINCT room_id FROM bookings WHERE (check_in < %s AND check_out > %s));",
            (f"'{check_out}'", f"'{check_in}'"),
            "GET",
        )
        

        for i in range(0, len(roomAvailable)):
            roomId.append(roomAvailable[i]["room_id"])

        chooseRoomInput = f"Choose a room {roomId}: "
        checkRoom = validationOption("room_id", chooseRoomInput, None, roomId)
        newBook["room_id"] = checkRoom

        specialRequest = input("Enter a special request (OPTIONAL): ")
        checkSpecialRequest = validationExists(
            "specialRequest", specialRequest, None
        )
        newBook["specialRequest"] = checkSpecialRequest

        newBook["status"] = "Check In"
        
        return newBook