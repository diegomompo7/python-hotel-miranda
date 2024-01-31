from models.models import *
from models.rooms import Rooms
from datetime import date, timedelta


class Bookings(Model):
    table = "bookings"

    def __init__(self, id, table):
        self.id = id
        self.table = table

    def create():
        name = input("What's your name: ")
        check_in = input("Date to entry (YYYY-MM-DD): ")
        hour_in = input("Date to entry (HH:MM): ")
        check_out = input("Date to entry (YYYY-MM-DD): ")
        hour_out = input("Date to entry (HH:MM): ")

        roomIdMessage = "Enter a id of room: "
        checkId = Model.validationPositive("room_id", roomIdMessage, None)
        booking_data = Rooms.view(checkId)

        specialRequest = input("Enter a special request (OPTIONAL): ")

        if type(booking_data) != list:
            roomId = checkId

        status = "Check In"

        newBook = Model.book(
            name,
            check_in,
            hour_in,
            check_out,
            hour_out,
            roomId,
            specialRequest,
            status,
            None,
        )

        Model.create(Bookings.table, newBook)

    def update(id):
        booking_data = Bookings.view(str(id))
        updateBook = booking_data
        statusBooking = ["Check In", "Check Out", "In Progress"]

        name = input(f"What's your name (default {updateBook['name']}): ")
        updateBook["name"] = Model.validationEmpty("name", name, booking_data)

        check_in = input(
            f"Date to entry (YYYY-MM-DD) (default {updateBook['check_in']}): "
        )
        
        
        updateBook["check_in"] = Model.validationEmpty("check_in", check_in, booking_data).strftime('%Y-%m-%d'),
        

        hour_in = input(f"Date to entry (HH:MM)  (default {updateBook['hour_in']}): ")
        updateBook["hour_in"] = Model.validationEmpty("hour_in", hour_in, booking_data).strftime('%H:%M'),
        

        check_out = input(
            f"Date to entry (YYYY-MM-DD)  (default {updateBook['check_out']}): "
        )
        updateBook["check_out"] = Model.validationEmpty("check_out", check_out, booking_data).strftime('%Y-%m-%d'),
        

        hour_out = input(f"Date to entry (HH:MM) (default {updateBook['hour_out']}): ")
        updateBook["hour_out"] = Model.validationEmpty("hour_out", hour_out, booking_data).strftime('%H:%M'),
        

        roomIdMessage = f"Enter a id of room (default {updateBook['room_id']}): "
        checkId = Model.validationPositive("room_id", roomIdMessage, booking_data)
        room_data = Rooms.view(checkId)

        if type(room_data) != list:
            roomId = checkId

        updateBook["room_id"] = roomId

        specialRequest = input(
            f"Enter a special request (OPTIONAL) (default {updateBook['specialRequest']}): "
        )

        updateBook['specialRequest'] = Model.validationEmpty("specialRequest", specialRequest, booking_data),

        statusMessage = (
            f"Enter a status {statusBooking} (default {booking_data['status']}): "
        )
        status = Model.validationOption(
            "status", statusMessage, booking_data, statusBooking
        )

        updateBook["status"] = status
        
        print(updateBook)

        Model.update(Bookings.table, updateBook, id)
