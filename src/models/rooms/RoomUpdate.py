from ..Model import *
from datetime import *
from ...validators.validators import *

def RoomUpdate(room_data, updateRoom):
        type = ["Single Bed", "Double Bed", "Double Superior", "Suite"]
        isOffer = ["YES", "NO"]
        roomStatus = ["Available", "Roomed"]

        room_data["photos"] = json.loads(room_data["photos"])
        photos = room_data["photos"]

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

        roomTypeInput = (
            f"Insert a room type {type} (default {room_data['roomType']}): "
        )
        roomType = validationOption("roomType", roomTypeInput, room_data, type)
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

        priceNightInput = (
            f"Insert a price per night (default {room_data['priceNight']}): "
        )
        priceNight = validationPositive(
            "priceNight", priceNightInput, room_data
        )
        updateRoom["priceNight"] = priceNight

        offerInput = (
            f"Insert if there's offer or not {isOffer} (default {room_data['offer']}): "
        )
        offer = validationOption("offer", offerInput, room_data, isOffer)
        updateRoom["offer"] = offer

        if offer == "YES":
            discountInput = f"Insert a discount (default {room_data['discount']}): "
            discount = validationPositive("discount", discountInput, room_data)
        else:
            discount = 0

        updateRoom["discount"] = discount

        cancellation = input(
            f"Insert a cancellation (default {room_data['cancellation']}): "
        )
        checkCancellation = validationExists(
            "cancellation", cancellation, room_data
        )
        updateRoom["cancellation"] = checkCancellation

        statusInput = (
            f"Insert a status {roomStatus} (default {room_data['status']}): "
        )
        status = validationOption("status", statusInput, room_data, roomStatus)
        updateRoom["status"] = status

        return updateRoom

def AmenitiesUpdate(amenitySelect, amenities_data, id):
    
    for i in range(0, len(amenitySelect)):
        amenities_data.append(amenitySelect[i]["amenity"])
    
    amenitiesInput = input(f"Insert amenities (default {amenities_data}): ")
    amenities = amenitiesInput.split(",")

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