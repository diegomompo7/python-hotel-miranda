from ..Model import *
from datetime import *
from ...validators.validators import *

def ContactUpdate(contact_data, updateContact):
        optionArchived = [False, True]
        
        userImg = input(f"Enter your image (default {contact_data['userImg']}): ")
        updateContact["userImg"] = validationExists(
            "userImg", userImg, contact_data
        )

        name = input(f"Enter your name (default {contact_data['name']}): ")
        updateContact["name"] = validationExists("name", name, contact_data)

        surname = input(f"Enter your surname (default {contact_data['surname']}): ")
        updateContact["surname"] = validationExists(
            "surname", surname, contact_data
        )

        email = input(f"Enter your email (default {contact_data['email']}): ")
        updateContact["email"] = validationExists("email", email, contact_data)

        phone = input(f"Enter your phone (default {contact_data['phone']}): ")
        updateContact["phone"] = validationExists("phone", phone, contact_data)

        dateMessage = f"Enter date when wrote the review (YYYY-MM-DD) (default {contact_data['date']}): "
        updateContact["date"] = validationDate('date', dateMessage, contact_data)

        subject = input(
            f"Enter the subject of review (default {contact_data['subject']}): "
        )
        updateContact["subject"] = validationExists(
            "subject", subject, contact_data
        )

        message = input(f"Enter your message (default {contact_data['message']}): ")
        updateContact["message"] = validationExists(
            "message", message, contact_data
        )

        messageStars = (
            f"Enter the stars (1-Lowest, 5-Highest) (default {contact_data['stars']}): "
        )
        stars = validationPositive("stars", messageStars, contact_data)

        while stars < 1 or 5 < stars:
            print("Please enter a number between 1 and 5.")
            stars = validationPositive("stars", messageStars, contact_data)

        updateContact["stars"] = stars

        isArchivedMessage = f"Enter if you want archived the review (default {contact_data['is_archived']}): "
        isArchived = validationOption(
            "is_archived", isArchivedMessage, contact_data, optionArchived
        )

        updateContact["is_archived"] = isArchived