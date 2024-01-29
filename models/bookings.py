from models.models import *
from models.rooms import Rooms

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
            name, check_in, hour_in, check_out, hour_out, roomId, specialRequest, status, None
        )

        Model.create(Bookings.table, newBook)

    def update(id):
        booking_data = Bookings.view(str(id))
        statusBooking = ["Check In", "Check Out", "In Progress"]

        name = input(f"What's your name (default {booking_data.get('name')}): ")
        check_in = input(
            f"Date to entry (YYYY-MM-DD) (default {booking_data.get('check_in')}): "
        )
        hour_in = input(
            f"Date to entry (HH:MM)  (default {booking_data.get('hour_in')}): "
        )
        check_out = input(
            f"Date to entry (YYYY-MM-DD)  (default {booking_data.get('check_out')}): "
        )
        hour_out = input(
            f"Date to entry (HH:MM) (default {booking_data.get('hour_out')}): "
        )
        
        roomIdMessage = "Enter a id of room: "
        checkId = Model.validationPositive("room_id", roomIdMessage, None)
        booking_data = Rooms.view(checkId)
        
        specialRequest = input("Enter a special request (OPTIONAL): ")
        
        if type(booking_data) != list:
            roomId = checkId
        
        
        specialRequest = input(
            f"Enter a special request (OPTIONAL) (default {booking_data.get('specialRequest')}): "
        )
        statusMessage = (
            f"Enter a status {statusBooking} (default {booking_data.get('status')}): "
        )
        status = Model.validationOption(
            "status", statusMessage, booking_data, statusBooking
        )

        updateBook =  Model.book(
            name,
            check_in,
            hour_in,
            check_out,
            hour_out,
            roomId,
            specialRequest,
            status,
            booking_data,
        )
