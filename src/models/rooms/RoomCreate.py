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

        roomTypeInput = f"Insert a room type {type}: "
        roomType = validationOption("roomType", roomTypeInput, None, type)
        newRoom["roomType"] = roomType

        roomNumberInput = "Insert a room number: "
        newRoom["roomNumber"] = validationEmpty(roomNumberInput, input(roomNumberInput))

        descriptionInput = "Insert a description: "
        newRoom["description"] = validationEmpty(descriptionInput, input(descriptionInput))

        priceNightInput = "Insert a price per night: "
        priceNight = validationPositive("priceNight", priceNightInput, None)
        newRoom["priceNight"] = priceNight

        offerInput = f"Insert if there's offer or not {isOffer}: "
        offer = validationOption(5, offerInput, None, isOffer)

        newRoom["offer"] = offer

        if offer == "YES":
            discountInput = "Insert a discount: "
            discount = validationPositive("discount", discountInput, None)
        else:
            discount = 0

        newRoom["discount"] = discount

        cancellationInput = input("Insert a cancellation: ")
        newRoom["cancellation"] = validationEmpty(cancellationInput, input(cancellationInput))
        newRoom["status"] = "Available"
        
        return newRoom

            
def AmenitiesCreate(newAmenity, idRoom):
    
        amenitiesInput = "Insert amenities: "
        amenitiesValue = validationEmpty(amenitiesInput, input(amenitiesInput))
        amenities = amenitiesValue.split(",")
        
        for amenity in amenities:
            newAmenity["amenity"] = amenity
            newAmenity["room_id"] = idRoom
            Model.create("amenities", newAmenity)