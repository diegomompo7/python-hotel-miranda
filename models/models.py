from abc import ABC, abstractmethod
import json
from datetime import date
from sql import executeQuery


class Model(ABC):
    table = None

    @classmethod
    def list(cls):
        result = executeQuery("SELECT * FROM %s ;", cls.table)
        for data in result:
            print(data)

    @classmethod
    def view(cls, id):
        result = executeQuery("SELECT * FROM %s WHERE id=%s;", (cls.table, id))
        for data in result:
            print(data)
            return data

        print(f"Error: JSON path for {cls.__name__}")

    @classmethod
    def delete(cls, id):
        pass

    @classmethod
    def create(cls, table, data):
        print(tuple(data.values()))
        result = executeQuery("INSERT INTO %s (%s) VALUES %s;", (table, ",".join(list(data.keys())), tuple(data.values())))
        print(result)

    @abstractmethod
    def update(self):
        pass

    def validationEmpty(input, value, data):
        if value is None:
            value = ""
            
        if value == "" and data is not None:
            return data.get(input)

        return value

    def validationOption(inputColumn, inputMessage, data, options):
        try:
            optionInput = input(inputMessage)

            checkOption = Model.validationEmpty(inputColumn, optionInput, data)
            
            print(checkOption)

            if options.count(checkOption) != 0:
                return checkOption

            print(f"Please enter a valid ption between this {options}.")
            return Model.validationOption(inputColumn, inputMessage, data, options)

        except ValueError:
            print(f"Please enter a valid ption between this {options}.")
            return Model.validationOption(inputColumn, inputMessage, data, options)

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
        roomIdValue,
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
            "room_id": roomIdValue,
            "specialRequest": Model.validationEmpty(
                "specialRequest", specialRequestValue, booking_data
            ),
            "status": statusValue,
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
            "roomType": roomTypeValue,
            "roomNumber": Model.validationEmpty(
                "roomNumber", roomNumberValue, room_data
            ),
            "description": Model.validationEmpty(
                "description", descriptionValue, room_data
            ),
            "offer": offerValue,
            "priceNight": priceNightValue,
            "discount": Model.validationEmpty("discount", discountValue, room_data),
            "cancellation": Model.validationEmpty(
                "cancellation", cancellationValue, room_data
            ),
            "amenities": amenitiesValue,
            "status": statusValue,
        }
        print(room)
        return room

    def contact(
        userImgValue,
        nameValue,
        surnameValue,
        emailValue,
        phoneValue,
        dateValue,
        subjectValue,
        messageValue,
        starsValue,
        isArchivedValue,
        contact_data,
    ):
        contact = {
            "userImg": Model.validationEmpty("userImg", userImgValue, contact_data),
            "name": Model.validationEmpty("name", nameValue, contact_data),
            "surname": Model.validationEmpty("surname", surnameValue, contact_data),
            "email": Model.validationEmpty("email", emailValue, contact_data),
            "phone": Model.validationEmpty("phone", phoneValue, contact_data),
            "date": Model.validationEmpty("date", dateValue, contact_data),
            "subject": Model.validationEmpty("subject", subjectValue, contact_data),
            "message": Model.validationEmpty("message", messageValue, contact_data),
            "stars": starsValue,
            "is_archived": Model.validationEmpty(
                "is_archived", isArchivedValue, contact_data
            ),
        }

        print(contact)
        return contact

    def user(
        photoValue,
        fullName,
        jobValue,
        emailValue,
        phoneValue,
        startDateValue,
        descriptionJobValue,
        statusValue,
        passwordValue,
        user_data,
    ):
        user = {
            "photo": Model.validationEmpty("photo", photoValue, user_data),
            "fullName": Model.validationEmpty("fullName", fullName, user_data),
            "job": jobValue,
            "email": Model.validationEmpty("email", emailValue, user_data),
            "phone": Model.validationEmpty("phone", phoneValue, user_data),
            "startDate": Model.validationEmpty("startDate", startDateValue, user_data),
            "descriptionJob": Model.validationEmpty("descriptionJob", descriptionJobValue, user_data),
            "status": statusValue,
            "password": Model.validationEmpty("password", passwordValue, user_data),
        }

        print(user)
        return user
