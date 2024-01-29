from abc import ABC, abstractmethod
import json
from datetime import date


class Model(ABC):
    json_path = None

    @classmethod
    def list(cls):
        if cls.json_path is not None:
            with open(cls.json_path, "r") as file:
                data = json.load(file)
            print(f"Listening {cls.__name__}")
            print(data)
            return data

        print(f"Error: JSON path for {cls.__name__}")

    @classmethod
    def view(cls, id):
        if cls.json_path is not None:
            with open(cls.json_path, "r") as file:
                data = json.load(file)
            for book in data:
                if int(id) == book.get("id"):
                    print(f"View {id}")
                    print(book)
                    return book

                print("id not found")
                return "id not found"

        print(f"Error: JSON path for {cls.__name__}")

    @classmethod
    def delete(cls, id):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass

    def validationEmpty(input, value, data):
        if value == "" and data is not None:
            print(data.get(input))
            return data.get(input)

        return value
            
    def validationPositive(inputColumn, inputMessage, data):
            try:
                
                if data is not None:
                    numberInput = input(inputMessage)
                else:
                    numberInput = int(input(inputMessage))
                
                checkNumber = Model.validationEmpty(inputColumn, numberInput, data)
        
                if type(checkNumber) == list:
                    return len(checkNumber)
            
                numberInput = int(checkNumber)
                
                if numberInput > 0:
                    return numberInput
                else:
                    print("Please enter a positive integer.")
                    return Model.validationPositive(inputColumn, inputMessage, data)
            except ValueError:
                print("Please enter a valid integer.")
                return Model.validationPositive(inputColumn, inputMessage, data)
        

    def book(
        nameValue,
        check_inValue,
        hour_inValue,
        check_outValue,
        hour_outValue,
        specialRequestValue,
        statusValue,
        booking_data,
    ):
        booking = {
            "name": Model.validationEmpty("name", nameValue, booking_data),
            "orderDate": date.today().isoformat()
            if booking_data is None
            else booking_data.get("orderDate"),
            "check_in": Model.validationEmpty("check_in", check_inValue, booking_data),
            "hour_in": Model.validationEmpty("hour_in", hour_inValue, booking_data),
            "check_out": Model.validationEmpty(
                "check_out", check_outValue, booking_data
            ),
            "hour_out": Model.validationEmpty("hour_out", hour_outValue, booking_data),
            "specialRequest": Model.validationEmpty(
                "specialRequest", specialRequestValue, booking_data
            ),
            "status": Model.validationEmpty("status", statusValue, booking_data)
        }

        return booking

    def room(
        photoValue,
        roomTypeValue,
        roomNumberValue,
        descriptionValue,
        offerValue,
        priceNightValue,
        discountValue,
        cancellationValue,
        amenitiesValue,
        statusValue,
        room_data,
    ):
        room = {
            "photo": photoValue,
            "roomType":  Model.validationEmpty("roomType", roomTypeValue, room_data),
            "roomNumber":  Model.validationEmpty("roomNumber", roomNumberValue, room_data),
            "description": Model.validationEmpty("description", descriptionValue, room_data),
            "offer": offerValue,
            "priceNight":  priceNightValue,
            "discount":  Model.validationEmpty("discount", discountValue, room_data),
            "cancellation":  Model.validationEmpty("cancellation", cancellationValue, room_data),
            "amenities":  amenitiesValue,
            "status":  Model.validationEmpty("status", statusValue, room_data),
        }
        print(room)
        return room