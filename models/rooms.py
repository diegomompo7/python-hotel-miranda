from models.models import *
from datetime import date


class Rooms(Model):
    json_path = "data/rooms.json"

    def __init__(self, id):
        self.id = id

    def create():
        amenities = []
        
        messagePhotos = "Insert a number of photos (from 3 to 5): "
        photos = Model.validationBetween("photos", messagePhotos, None)
        
        roomType = input("Insert a room type: ")
        roomNumber = input("Insert a room number: ")
        description = input("Insert a description: ")
        
        messagePriceNight = "Insert a price per night: "
        priceNight = Model.validationPositive("priceNight", messagePriceNight, None)

        offer = input("Insert if there's offer or not (YES OR NO): ")
        if offer == "YES":
                messageDiscount = "Insert a discount: "
                discountValue = Model.validationPositive("discount", messageDiscount, None)
        else:
            discountValue = 0

        cancellation = input("Insert a cancellation: ")

        messageNumberAmenities = "Insert a number of amenities: "
        numberAmenities = Model.validationPositive("amenities", messageNumberAmenities, None)
                
        if numberAmenities > 0:
            for i in range(0, numberAmenities):
                amenity = input(f"Insert amenity number {i+1}: ")
                amenities.append(amenity)
            
        status = "Available"
        
        Model.room(photos, roomType, roomNumber, description, offer, priceNight, discountValue, cancellation, amenities, status, None)

    def update(id):
        room_data = Rooms.view(str(id))
        
        photos = room_data.get("photos")
        amenities = room_data.get("amenities")

        messagePhotos = f"Insert a number of photos (from 3 to 5) (default {len(photos)}): "
        numberPhotos = Model.validationPositive("photos", messagePhotos, room_data)

        if 3 <= numberPhotos <= 5:
            for i in range(0, numberPhotos):
                    photo = input(f"Insert the photo number {i+1}: ")
                    photos.append(photo)
                    
            if numberPhotos < len(photos):
                    photos = photos[0:numberPhotos]
        else:
            print("Please enter a number between 3 and 5.")
            return Model.validationPositive("photos", messagePhotos, room_data)

        roomType = input(
            f"Insert a room type (default {room_data.get('roomType')}): "
        )
        roomNumber = input(
            f"Insert a room number (default {room_data.get('roomNumber')}): "
        ) 
        description = input(
            f"Insert a description (default {room_data.get('description')}): "
        )
        messagePriceNight = f"Insert a price per night (default {room_data.get('priceNight')}): "
        priceNight = Model.validationPositive("priceNight", messagePriceNight, room_data)

        offer = input(
            f"Insert if there's offer or not (YES OR NO) (default {room_data.get('offer')}): "
        )
        checkOffer = Model.validationEmpty("offer", offer, room_data)
        if checkOffer == "YES":
                messageDiscount = f"Insert a discount (default {room_data.get('discount')}): "
                discount = Model.validationPositive("discount", messageDiscount, room_data)
        else:
            discount = 0

        cancellation = input(
            f"Insert a cancellation (default {room_data.get('cancellation')}): "
        )

        messageNumberAmenities = f"Insert a number of amenities (default {len(amenities)}): "

        numberAmenities = Model.validationPositive("amenities", messageNumberAmenities, room_data)
    
        
        if numberAmenities > 0:
            for i in range(0, numberAmenities):
                amenity = (
                    input(
                        f"Insert amenity number {i+1} (default {amenities[i]}): "
                        )
                        or amenities[i]
                    )
                amenities[i] = amenity
                
            if numberAmenities < len(amenities):
                amenities = amenities[0:numberAmenities]   

        status = input(
            f"Inter a status (Available or Booked) (default {room_data.get('status')}): "
        )

        Model.room(photos, roomType, roomNumber, description, offer, priceNight, discount, cancellation, amenities, status, room_data)

