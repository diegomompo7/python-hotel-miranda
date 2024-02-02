from ..Model import *
from datetime import *
from ...validators.validators import *

def BookingUpdate(booking_data, updateBook, roomId):
        statusBooking = ["Check In", "Check Out", "In Progress"]

        name = input(f"What's your name (default {updateBook['name']}): ")
        updateBook["name"] = validationExists("name", name, booking_data)

        checkInMessage = f"Date to entry (YYYY-MM-DD) (default {updateBook['check_in']}): "
        
        updateBook["check_in"] = validationDate('check_in', checkInMessage, booking_data)

        hour_in = input(f"Date to entry (HH:MM)  (default {updateBook['hour_in']}): ")
        updateBook["hour_in"] = validationExists("hour_in", hour_in, booking_data)

        checkOutMessage = f"Date to entry (YYYY-MM-DD)  (default {updateBook['check_out']}): "
        updateBook["check_out"] = validationDate('check_out', checkOutMessage, updateBook)

        hour_out = input(f"Date to entry (HH:MM) (default {updateBook['hour_out']}): ")
        updateBook["hour_out"] = validationExists(
            "hour_out", hour_out, booking_data
        )

        roomAvailable = executeQuery(
            "SELECT room_id FROM bookings WHERE check_in > %s OR check_out < %s;",
            (f'\'{updateBook["check_out"]}\'', f'\'{updateBook["check_in"]}\''),
            "GET",
        )

        for i in range(0, len(roomAvailable)):
            roomId.append(roomAvailable[i]["room_id"])

        chooseRoomMessage = (
            f"Choose a room {roomId} (defualt {booking_data['room_id']}): "
        )
        checkRoom = validationOption(
            "room_id", chooseRoomMessage, booking_data, roomId
        )
        updateBook["room_id"] = checkRoom

        specialRequest = input(
            f"Enter a special request (OPTIONAL) (default {updateBook['specialRequest']}): "
        )
        updateBook["specialRequest"] = validationExists(
            "specialRequest", specialRequest, booking_data
        )

        statusMessage = (
            f"Enter a status {statusBooking} (default {booking_data['status']}): "
        )
        status = validationOption(
            "status", statusMessage, booking_data, statusBooking
        )
        updateBook["status"] = status
        
        return updateBook
        