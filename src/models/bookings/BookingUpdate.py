from ..Model import *
from datetime import *
from ...validators.validators import *

def BookingUpdate(booking_data, updateBook, roomId):
        statusBooking = ["Check In", "Check Out", "In Progress"]

        name = input(f"What's your name (default {updateBook['name']}): ")
        updateBook["name"] = validationExists("name", name, booking_data)

        checkInInput = f"Date to entry (YYYY-MM-DD) (default {updateBook['check_in']}): "
        
        updateBook["check_in"] = validationDate('check_in', checkInInput, input(checkInInput), booking_data)

        hourInInput = f"Time to entry (HH:MM)  (default {updateBook['hour_in']}): "
        updateBook["hour_in"] = validationTime('hour_in', hourInInput, input(hourInInput), booking_data)

        checkOutInput = f"Date to out (YYYY-MM-DD)  (default {updateBook['check_out']}): "
        updateBook["check_out"] = validationDate('check_out', checkOutInput, input(checkOutInput), updateBook)

        hourOutInput = f"Time to out (HH:MM) (default {updateBook['hour_out']}): "
        updateBook["hour_out"] = validationTime('hour_out', hourOutInput, input(hourOutInput), booking_data)

        roomAvailable = executeQuery(
            "SELECT DISTINCT room_id FROM bookings WHERE room_id NOT IN (SELECT DISTINCT room_id FROM bookings WHERE (check_in < %s AND check_out > %s));",
            (f'\'{updateBook["check_out"]}\'', f'\'{updateBook["check_in"]}\''),
            "GET",
        )

        for i in range(0, len(roomAvailable)):
            roomId.append(roomAvailable[i]["room_id"])
        
        roomId.append(booking_data["room_id"])

        chooseRoomInput = (
            f"Choose a room {roomId} (defualt {booking_data['room_id']}): "
        )
        checkRoom = validationOption(
            "room_id", chooseRoomInput, booking_data, roomId
        )
        updateBook["room_id"] = checkRoom

        specialRequest = input(
            f"Enter a special request (OPTIONAL) (default {updateBook['specialRequest']}): "
        )
        updateBook["specialRequest"] = validationExists(
            "specialRequest", specialRequest, booking_data
        )

        statusInput = (
            f"Enter a status {statusBooking} (default {booking_data['status']}): "
        )
        status = validationOption(
            "status", statusInput, booking_data, statusBooking
        )
        updateBook["status"] = status
        
        return updateBook
        