from ..Model import *
from datetime import *
from ...validators.validators import *

def ContactCreate(newContact):
        userImg = input("Enter your image: ")
        newContact["userImg"] = userImg

        name = input("Enter your name: ")
        newContact["name"] = name

        surname = input("Enter your surname: ")
        newContact["surname"] = surname

        email = input("Enter your email: ")
        newContact["email"] = email

        phone = input("Enter your phone: ")
        newContact["phone"] = phone

        dateMessage = "Enter date when wrote the review (YYYY-MM-DD): "
        newContact["date"] = validationDate('date', dateMessage, input(dateMessage), None)

        subject = input("Enter the subject of review: ")
        newContact["subject"] = subject

        message = input("Enter your message: ")
        newContact["message"] = message

        messageStars = "Enter the stars (1-Lowest, 5-Highest): "

        stars = validationPositive("stars", messageStars, None)

        while 5 < stars:
            print("Please enter a number between 1 and 5.")
            stars = validationPositive("photos", messageStars, None)

        newContact["stars"] = stars

        newContact["is_archived"] = False