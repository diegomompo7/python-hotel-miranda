from ..Model import *
from .BookingCreate import BookingCreate
from .BookingUpdate import BookingUpdate


class Bookings(Model):
    table = "bookings"

    def __init__(self, id, table):
        self.id = id
        self.table = table

    @classmethod
    def create(cls):
        roomId = []
        newBook = {}
        fields = executeQuery("SHOW FIELDS FROM %s", Bookings.table, "GET")
        for i in range(1, len(fields)):
            newBook[fields[i]["Field"]] = ""
            
        super(Bookings, cls).create(cls.table, BookingCreate(newBook, roomId))

    @classmethod
    def update(cls, id):
        roomId = []
        booking_data = Bookings.view(str(id))
        updateBook = booking_data

        super(Bookings, cls).update(cls.table,  BookingUpdate(booking_data, updateBook, roomId), id)
