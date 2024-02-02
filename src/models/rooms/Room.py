from ..Model import *
from src.db.sql import executeQuery
from .RoomCreate import RoomCreate, AmenitiesCreate
from .RoomUpdate import RoomUpdate, AmenitiesUpdate


class Rooms(Model):
    table = "rooms"

    def __init__(self, id, table):
        self.id = id
        self.table = table

    @classmethod
    def create(cls):
        newRoom = {}
        newAmenity = {}

        fields = executeQuery("SHOW FIELDS FROM %s", Rooms.table, "GET")
        for i in range(1, len(fields)):
            newRoom[fields[i]["Field"]] = ""

        fieldsAmenities = executeQuery("SHOW FIELDS FROM %s", "amenities", "GET")
        for i in range(1, len(fieldsAmenities)):
            newAmenity[fieldsAmenities[i]["Field"]] = ""
            
        idRoom = super(Rooms, cls).create(cls.table, RoomCreate(newRoom))
        AmenitiesCreate(newAmenity, idRoom)


    @classmethod
    def update(cls, id):
        room_data = Rooms.view(str(id))
        amenitySelect = executeQuery(
            "SELECT amenity, room_id FROM amenities WHERE room_id=%s", id, "GET"
        )
        amenities_data = []
        updateRoom = room_data
        
        super(Rooms, cls).update(cls.table, RoomUpdate(room_data, updateRoom))
        AmenitiesUpdate(amenitySelect, amenities_data, id)

