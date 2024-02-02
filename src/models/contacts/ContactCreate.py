from ..Model import *
from datetime import *
from ...validators.validators import *

def ContactCreate(newContact):
        userImgInput = "Enter your image: "
        newContact["userImg"] = validationEmpty(userImgInput, input(userImgInput))

        nameInput = "Enter your name: "
        newContact["name"] = validationEmpty(nameInput, input(nameInput))

        surnameInput = "Enter your surname: "
        newContact["surname"] = validationEmpty(surnameInput, input(surnameInput))

        emailInput = "Enter your email: "
        newContact["email"] = validationEmail("email", emailInput, input(emailInput), None)

        phoneInput = "Enter your phone: "
        newContact["phone"] = validationPhone("phone", phoneInput, input(phoneInput), None)

        dateInput = "Enter date when wrote the review (YYYY-MM-DD): "
        newContact["date"] = validationDate('date', dateInput, input(dateInput), None)

        subjectInput = "Enter the subject of review: "
        newContact["subject"] = validationEmpty(subjectInput, input(subjectInput))

        messageInput = "Enter your message: "
        newContact["message"] = validationEmpty(messageInput, input(messageInput))

        starsInput = "Enter the stars (1-Lowest, 5-Highest): "

        stars = validationPositive("stars", starsInput, None)

        while 5 < stars:
            print("Please enter a number between 1 and 5.")
            stars = validationPositive("photos", starsInput, None)

        newContact["stars"] = stars

        newContact["is_archived"] = False
        
        return newContact