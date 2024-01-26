from models.models import *
from datetime import date


class Rooms(Model):
    json_path = "data/rooms.json"

    def __init__(self, id):
        self.id = id

    def create():
        photos = []
        amenities = []
        numberPhotos = int(input("Insert a number of photos (from 3 to 5): "))

        while True:
            try:
                numberPhotos = int(input("Insert a number of photos (from 3 to 5): "))
                if 3 <= numberPhotos <= 5:
                    for i in range(0, numberPhotos):
                        photo = input(f"Insert the photo number {i+1}: ")
                        photos.append(photo)
                    break
                else:
                    print("Please enter a number between 3 and 5.")
            except ValueError:
                print("Please enter a valid integer.")

        roomType = input("Insert a room type: ")
        roomNumber = input("Insert a room number: ")
        description = input("Insert a description: ")

        while True:
            try:
                priceNight = int(input("Insert a price per night: "))
                if priceNight > 0:
                    break
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Please enter a valid integer.")

        offer = input("Insert if there's offer or not (YES OR NO): ")
        if offer == "YES":
            while True:
                try:
                    discount = int(input("Insert a discount: "))
                    if discount > 0:
                        break
                    else:
                        print("Please enter a positive integer.")
                except ValueError:
                    print("Please enter a valid integer.")
        else:
            discount = 0

        cancellation = input("Insert a cancellation: ")

        while True:
            try:
                numberAmenities = int(input("Insert a number of amenities: "))
                if numberAmenities > 0:
                    for i in range(0, numberAmenities):
                        amenity = input(f"Insert amenity number {i+1}: ")
                        amenities.append(amenity)
                    break
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Please enter a valid integer.")

        status = "Available"

        newRoom = {
            "photo": photos,
            "roomType": roomType,
            "roomNumber": roomNumber,
            "description": description,
            "offer": offer,
            "priceNight": priceNight,
            "discount": discount,
            "cancellation": cancellation,
            "amenities": amenities,
            "status": status,
        }

        print(newRoom)
        return newRoom

    def update(id):
        room_data = Rooms.view(str(id))

        photos = room_data.get("photos")
        amenities = room_data.get("amenities")

        while True:
            try:
                numberPhotos_input = input("Insert a number of photos (from 3 to 5): ")
                if numberPhotos_input:
                    numberPhotos = int(numberAmenities_input)
                else:
                    numberPhotos = len(photos)
                if numberPhotos is None or 3 <= numberPhotos <= 5:
                    for i in range(0, numberPhotos):
                        photo = input(f"Insert the photo number {i+1}: ")
                        photos.append(photo)
                    break
                else:
                    print("Please enter a number between 3 and 5.")
            except ValueError:
                print("Please enter a valid integer.")

        if numberPhotos < len(photos):
            photos = photos[0:numberPhotos]

        roomType = input(
            f"Insert a room type (default {room_data.get('roomType')}): "
        ) or room_data.get("roomType")
        roomNumber = input(
            f"Insert a room number (default {room_data.get('roomNumber')}): "
        ) or room_data.get("roomNumber")
        description = input(
            f"Insert a description (default {room_data.get('description')}): "
        ) or room_data.get("description")
        priceNight = int(
            input(f"Insert a price per night (default {room_data.get('priceNight')}): ")
            or room_data.get("priceNight")
        )

        offer = input(
            f"Insert if there's offer or not (YES OR NO) (default {room_data.get('offer')}): "
        ) or room_data.get("offer")
        if offer == "YES":
            discount = int(
                input(f"Insert a discount (default {room_data.get('discount')}): ")
                or room_data.get("discount")
            )
        else:
            discount = 0

        cancellation = input(
            f"Insert a cancellation (default {room_data.get('cancellation')}): "
        ) or room_data.get("cancellation")

        while True:
            try:
                numberAmenities_input = input(
                    f"Insert a number of amenities (default {len(amenities)}): "
                )

                if numberAmenities_input:
                    numberAmenities = int(numberAmenities_input)
                else:
                    numberAmenities = len(amenities)
                if numberAmenities is None or numberAmenities > 0:
                    for i in range(0, numberAmenities):
                        amenity = (
                            input(
                                f"Insert amenity number {i+1} (default {amenities[i]}): "
                            )
                            or amenities[i]
                        )
                        amenities[i] = amenity
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Please enter a valid integer.")

        if numberAmenities < len(amenities):
            amenities = amenities[0:numberAmenities]

        status = input(
            f"Inter a status (Available or Booked) (default {room_data.get('status')}): "
        ) or room_data.get("status")

        updateRoom = {
            "photos": photos,
            "roomType": roomType,
            "roomNumber": roomNumber,
            "description": description,
            "offer": offer,
            "priceNight": priceNight,
            "discount": discount,
            "cancellation": cancellation,
            "amenities": amenities,
            "status": status,
        }

        print(updateRoom)
        return updateRoom
