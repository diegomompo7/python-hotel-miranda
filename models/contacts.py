from models.models import *
from datetime import date


class Contacts(Model):
    table = "contacts"

    def __init__(self, id):
        self.id = id

    def create():
        userImg = input("Enter your image: ")
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone: ")
        date = input("Enter date when wrote the review (YYYY-MM-DD): ")
        subject = input("Enter the subject of review: ")
        message = input("Enter your message: ")

        messageStars = "Enter the stars (1-Lowest, 5-Highest): "

        stars = Model.validationPositive("stars", messageStars, None)

        while 5 < stars:
            print("Please enter a number between 1 and 5.")
            stars = Model.validationPositive("photos", messageStars, None)

        isArchived = False

        Model.contact(
            userImg,
            name,
            surname,
            email,
            phone,
            date,
            subject,
            message,
            stars,
            isArchived,
            None,
        )

    def update(id):
        contact_data = Contacts.view(str(id))

        userImg = input(f"Enter your image (default {contact_data.get('userImg')}): ")
        name = input(f"Enter your name (default {contact_data.get('name')}): ")
        surname = input(f"Enter your surname (default {contact_data.get('surname')}): ")
        email = input(f"Enter your email (default {contact_data.get('email')}): ")
        phone = input(f"Enter your phone (default {contact_data.get('phone')}): ")
        date = input(
            f"Enter date when wrote the review (YYYY-MM-DD) (default {contact_data.get('date')}): "
        )
        subject = input(
            f"Enter the subject of review (default {contact_data.get('subject')}): "
        )
        message = input(f"Enter your message (default {contact_data.get('message')}): ")

        messageStars = f"Enter the stars (1-Lowest, 5-Highest) (default {contact_data.get('stars')}): "
        stars = Model.validationPositive("photos", messageStars, None)

        while stars < 1 or 5 < stars:
            print("Please enter a number between 1 and 5.")
            stars = Model.validationPositive("photos", messageStars, None)

        isArchived = input(
            f"Enter if you want archived the review (default {contact_data.get('is_archived')}): "
        )

        Model.contact(
            userImg,
            name,
            surname,
            email,
            phone,
            date,
            subject,
            message,
            stars,
            isArchived,
            contact_data,
        )
