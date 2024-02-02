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

        emailInput = f"Enter your email (default {contact_data['email']}): "
        updateContact["email"] = validationEmail("email", emailInput, input(emailInput), contact_data)
        
        phoneInput = f"Enter your phone (default {contact_data['phone']}): "
        updateContact["phone"] = validationPhone("phone", phoneInput, input(phoneInput), contact_data)

        dateInput = f"Enter date when wrote the review (YYYY-MM-DD) (default {contact_data['date']}): "
        updateContact["date"] = validationDate('date', dateInput, input(dateInput), contact_data)

        subject = input(
            f"Enter the subject of review (default {contact_data['subject']}): "
        )
        updateContact["subject"] = validationExists(
            "subject", subject, contact_data
        )

        messageInput = input(f"Enter your message (default {contact_data['message']}): ")
        updateContact["message"] = validationExists(
            "message", messageInput, contact_data
        )

        starsInput = input(
            f"Enter the stars (1-Lowest, 5-Highest) (default {contact_data['stars']}): "
        )
        stars = validationPositive("stars", starsInput, contact_data)

        while stars < 1 or 5 < stars:
            print("Please enter a number between 1 and 5.")
            stars = validationPositive("stars", starsInput, contact_data)

        updateContact["stars"] = stars

        isArchivedInput = f"Enter if you want archived the review (default {contact_data['is_archived']}): "
        isArchived = validationOption(
            "is_archived", isArchivedInput, contact_data, optionArchived
        )

        updateContact["is_archived"] = isArchived
        
        return updateContact