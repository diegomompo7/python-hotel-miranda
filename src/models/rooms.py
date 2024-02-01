from .models import *
from sql import executeQuery

from ..validators.validatorExists import *
from ..validators.validatorPositive import *
from ..validators.validatorOptions import *


class Rooms(Model):
    table = "rooms"

    def __init__(self, id):
        self.id = id

    def create():
        newRoom = {}
        newAmenity = {}

        fields = executeQuery("SHOW FIELDS FROM %s", Rooms.table, "GET")
        for i in range(1, len(fields)):
            newRoom[fields[i]["Field"]] = ""

        fieldsAmenities = executeQuery("SHOW FIELDS FROM %s", "amenities", "GET")
        for i in range(1, len(fieldsAmenities)):
            newAmenity[fieldsAmenities[i]["Field"]] = ""

        photos = []
        type = ["Single Bed", "Double Bed", "Double Superior", "Suite"]
        isOffer = ["YES", "NO"]
        messagePhotos = "Insert a number of photos (from 3 to 5): "

        numberPhotos = validationPositive(1, messagePhotos, None)

        while numberPhotos < 3 or 5 < numberPhotos:
            print("Please enter a number between 3 and 5.")
            numberPhotos = validationPositive(1, messagePhotos, None)

        for i in range(0, numberPhotos):
            photo = input(f"Insert the photo number {i+1}: ")
            photos.append(f"{photo}")

        newRoom["photos"] = f"{json.dumps(photos)}"

        roomTypeMessage = f"Insert a room type {type}: "
        roomType = validationOption("roomType", roomTypeMessage, None, type)
        newRoom["roomType"] = roomType

        roomNumber = input("Insert a room number: ")
        newRoom["roomNumber"] = roomNumber

        description = input("Insert a description: ")
        newRoom["description"] = description

        messagePriceNight = "Insert a price per night: "
        priceNight = validationPositive("priceNight", messagePriceNight, None)
        newRoom["priceNight"] = priceNight

        offerMessage = f"Insert if there's offer or not {isOffer}: "
        offer = validationOption(5, offerMessage, None, isOffer)

        newRoom["offer"] = offer

        if offer == "YES":
            messageDiscount = "Insert a discount: "
            discount = validationPositive("discount", messageDiscount, None)
        else:
            discount = 0

        newRoom["discount"] = discount

        cancellation = input("Insert a cancellation: ")
        newRoom["cancellation"] = cancellation

        amenitiesInput = input(f"Insert amenities: ")
        amenities = amenitiesInput.split(",")

        newRoom["status"] = "Available"

        idRoom = Model.create(Rooms.table, newRoom)

        for amenity in amenities:
            newAmenity["amenity"] = amenity
            newAmenity["room_id"] = idRoom
            Model.create("amenities", newAmenity)

    def update(id):
        room_data = Rooms.view(str(id))
        amenitySelect = executeQuery(
            "SELECT amenity, room_id FROM amenities WHERE room_id=%s", id, "GET"
        )
        amenities_data = []
        updateRoom = room_data

        type = ["Single Bed", "Double Bed", "Double Superior", "Suite"]
        isOffer = ["YES", "NO"]
        roomStatus = ["Available", "Booked"]

        room_data["photos"] = json.loads(room_data["photos"])
        photos = room_data["photos"]

        for i in range(0, len(amenitySelect)):
            amenities_data.append(amenitySelect[i]["amenity"])

        messagePhotos = (
            f"Insert a number of photos (from 3 to 5) (default {len(photos)}): "
        )
        numberPhotos = validationPositive("photos", messagePhotos, room_data)

        while numberPhotos < 3 or 5 < numberPhotos:
            print("Please enter a number between 3 and 5.")
            numberPhotos = validationPositive("photos", messagePhotos, room_data)

        for i in range(0, numberPhotos):
            photo = (
                input(f"Insert the photo number {i+1} default ({photos[i]}): ")
                or photos[i]
            )
            photos.append(f"{photo}")

        if numberPhotos < len(photos):
            photos = photos[0:numberPhotos]

        updateRoom["photos"] = json.dumps(photos)

        roomTypeMessage = (
            f"Insert a room type {type} (default {room_data['roomType']}): "
        )
        roomType = validationOption("roomType", roomTypeMessage, room_data, type)
        updateRoom["roomType"] = roomType

        roomNumber = input(
            f"Insert a room number (default {room_data['roomNumber']}): "
        )
        checkRoomNumber = validationExists("roomNumber", roomNumber, room_data)
        updateRoom["roomNumber"] = checkRoomNumber

        description = input(
            f"Insert a description (default {room_data['description']}): "
        )
        checkDescription = validationExists("description", description, room_data)
        updateRoom["description"] = checkDescription

        messagePriceNight = (
            f"Insert a price per night (default {room_data['priceNight']}): "
        )
        priceNight = validationPositive(
            "priceNight", messagePriceNight, room_data
        )
        updateRoom["priceNight"] = priceNight

        offerMessage = (
            f"Insert if there's offer or not {isOffer} (default {room_data['offer']}): "
        )
        offer = validationOption("offer", offerMessage, room_data, isOffer)
        updateRoom["offer"] = offer

        if offer == "YES":
            messageDiscount = f"Insert a discount (default {room_data['discount']}): "
            discount = validationPositive("discount", messageDiscount, room_data)
        else:
            discount = 0

        updateRoom["discount"] = discount

        cancellation = input(
            f"Insert a cancellation (default {room_data['cancellation']}): "
        )
        checkRoomNumber = validationExists(
            "cancellation", cancellation, room_data
        )
        updateRoom["cancellation"] = checkRoomNumber

        amenitiesInput = input(f"Insert amenities (default {amenities_data}): ")
        amenities = amenitiesInput.split(",")

        statusMessage = (
            f"Insert a status {roomStatus} (default {room_data['status']}): "
        )
        status = validationOption("status", statusMessage, room_data, roomStatus)
        updateRoom["status"] = status

        Model.update(Rooms.table, updateRoom, id)

        if amenitiesInput == "":
            amenities = amenities_data

        for amenity in amenities:
            if amenity not in amenities_data:
                Model.create("amenities", {"amenity": amenity, "room_id": id})

        for amenity in amenities_data:
            if amenity not in amenities:
                executeQuery(
                    "DELETE FROM amenities WHERE amenity=%s and room_id=%s",
                    (f"'{amenity}'", id),
                    "DELETE",
                )
