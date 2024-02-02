from ..Model import *
from datetime import *
from ...validators.validators import *

def RoomCreate(newRoom):
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
        newRoom["status"] = "Available"
        
        return newRoom

            
def AmenitiesCreate(newAmenity, idRoom):
    
        amenitiesInput = input(f"Insert amenities: ")
        amenities = amenitiesInput.split(",")
        
        for amenity in amenities:
            newAmenity["amenity"] = amenity
            newAmenity["room_id"] = idRoom
            Model.create("amenities", newAmenity)