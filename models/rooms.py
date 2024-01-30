from models.models import *
from sql import executeQuery


class Rooms(Model):
    table = "rooms"

    def __init__(self, id):
        self.id = id

    def create():
        
        
        
        photos = []
        type = ["Single Bed", "Double Bed", "Double Superior", "Suite"]
        isOffer = ["YES", "NO"]

        messagePhotos = "Insert a number of photos (from 3 to 5): "
        
        numberPhotos = Model.validationPositive(1, messagePhotos, None)

        while numberPhotos < 3 or 5 < numberPhotos:
            print("Please enter a number between 3 and 5.")
            numberPhotos = Model.validationPositive(1, messagePhotos, None)

        for i in range(numberPhotos):
            photo = input(f"Insert the photo number {i+1}: ")
            photos.append(f"{photo}")
            
        print(photos)

        roomTypeMessage = f"Insert a room type {type}: "
        roomType = Model.validationOption(2, roomTypeMessage, None, type)

        roomNumber = input("Insert a room number: ")
        description = input("Insert a description: ")

        messagePriceNight = "Insert a price per night: "
        priceNight = Model.validationPositive(6, messagePriceNight, None)

        offerMessage = f"Insert if there's offer or not {isOffer}: "
        offer = Model.validationOption(5, offerMessage, None, isOffer)

        if offer == "YES":
            messageDiscount = "Insert a discount: "
            discountValue = Model.validationPositive(7, messageDiscount, None)
        else:
            discountValue = 0

        cancellation = input("Insert a cancellation: ")
        
        amenitiesInput = input(f"Insert amenities: ")
        checkAmenities = Model.validationEmpty(1, amenitiesInput, None)
        amenities = checkAmenities.split(",")
        
        status = "Available"

        newRoom = Model.room(
            f'{json.dumps(photos)}',
            roomType,
            roomNumber,
            description,
            offer,
            priceNight,
            discountValue,
            cancellation,
            status,
            None,
        )
        
        idRoom = Model.create(Rooms.table, newRoom)
        
        for amenity in amenities:
            Model.create("amenities", {"amenity": amenity, "room_id": idRoom})
        

    def update(id):
        room_data = Rooms.view(str(id))
        amenities_data = executeQuery("SELECT GROUP_CONCAT(amenity), room_id FROM amenities RIGHT JOIN rooms ON room_id = rooms.id WHERE rooms.id = %s;", id, "GET")
        
        type = ["Single Bed", "Double Bed", "Double Superior", "Suite"]
        isOffer = ["YES", "NO"]
        roomStatus = ["Available", "Booked"]
        photos = room_data[1]

        messagePhotos = (
            f"Insert a number of photos (from 3 to 5) (default {len(photos)}): "
        )
        numberPhotos = Model.validationPositive("photos", messagePhotos, room_data)

        while numberPhotos < 3 or 5 < numberPhotos:
            print("Please enter a number between 3 and 5.")
            numberPhotos = Model.validationPositive("photos", messagePhotos, None)

        for i in range(numberPhotos):
            photo = input(f"Insert the photo number {i+1}: ")
            photos.append(photo)

        if numberPhotos < len(photos):
            photos = photos[0:numberPhotos]

        roomTypeMessage = (
            f"Insert a room type {type} (default {room_data.get('roomType')}): "
        )
        roomType = Model.validationOption("roomType", roomTypeMessage, room_data, type)

        roomNumber = input(
            f"Insert a room number (default {room_data.get('roomNumber')}): "
        )
        description = input(
            f"Insert a description (default {room_data.get('description')}): "
        )
        messagePriceNight = (
            f"Insert a price per night (default {room_data.get('priceNight')}): "
        )
        priceNight = Model.validationPositive(
            "priceNight", messagePriceNight, room_data
        )

        offerMessage = f"Insert if there's offer or not {isOffer} (default {room_data.get('offer')}): "
        offer = Model.validationOption("offer", offerMessage, room_data, isOffer)

        if offer == "YES":
            messageDiscount = (
                f"Insert a discount (default {room_data.get('discount')}): "
            )
            discount = Model.validationPositive("discount", messageDiscount, room_data)
        else:
            discount = 0

        cancellation = input(
            f"Insert a cancellation (default {room_data.get('cancellation')}): "
        )

        amenities = input(f"Insert amenities: ")

        statusMessage = (
            f"Insert a status {roomStatus} (default {room_data.get('status')}): "
        )
        status = Model.validationOption("status", statusMessage, room_data, roomStatus)

        Model.room(
            photos,
            roomType,
            roomNumber,
            description,
            offer,
            priceNight,
            discount,
            cancellation,
            status,
            room_data,
        )
