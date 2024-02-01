from models.models import *
from datetime import date


class Contacts(Model):
    table = "contacts"

    def __init__(self, id):
        self.id = id

    def create():
        
        newContact = {}
        fields = executeQuery("SHOW FIELDS FROM %s", Contacts.table, "GET")
        for i in range(1, len(fields)):
            newContact[fields[i]["Field"]] = ""
        
        userImg = input("Enter your image: ")
        newContact['userImg'] = userImg
        
        name = input("Enter your name: ")
        newContact['name'] = name
        
        surname = input("Enter your surname: ")
        newContact['surname'] = surname
        
        email = input("Enter your email: ")
        newContact['email'] = email
        
        phone = input("Enter your phone: ")
        newContact['phone'] = phone
        
        date = input("Enter date when wrote the review (YYYY-MM-DD): ")
        newContact['date'] = date
        
        subject = input("Enter the subject of review: ")
        newContact['subject'] = subject
        
        message = input("Enter your message: ")
        newContact['message'] = message

        messageStars = "Enter the stars (1-Lowest, 5-Highest): "

        stars = Model.validationPositive("stars", messageStars, None)

        while 5 < stars:
            print("Please enter a number between 1 and 5.")
            stars = Model.validationPositive("photos", messageStars, None)
            
        newContact['stars'] = stars

        newContact['is_archived'] = False

        Model.create(Contacts.table, newContact)
        
    def update(id):
        contact_data = Contacts.view(str(id))
        updateContact = contact_data
        optionArchived = [False, True]

        userImg = input(f"Enter your image (default {contact_data['userImg']}): ")
        updateContact['userImg'] = Model.validationEmpty("userImg", userImg, contact_data)
        
        name = input(f"Enter your name (default {contact_data['name']}): ")
        updateContact['name'] = Model.validationEmpty("name", name, contact_data)
        
        surname = input(f"Enter your surname (default {contact_data['surname']}): ")
        updateContact['surname'] = Model.validationEmpty("surname", surname, contact_data)
        
        email = input(f"Enter your email (default {contact_data['email']}): ")
        updateContact['email'] = Model.validationEmpty("email", email, contact_data)
        
        phone = input(f"Enter your phone (default {contact_data['phone']}): ")
        updateContact['phone'] = Model.validationEmpty("phone", phone, contact_data)
        
        date = input(f"Enter date when wrote the review (YYYY-MM-DD) (default {contact_data['date']}): ")
        updateContact['date'] = Model.validationEmpty("date", date, contact_data)
        
        subject = input(f"Enter the subject of review (default {contact_data['subject']}): ")
        updateContact['subject'] = Model.validationEmpty("subject", subject, contact_data)
        
        message = input(f"Enter your message (default {contact_data['message']}): ")
        updateContact['message'] = Model.validationEmpty("message", message, contact_data)

        messageStars = f"Enter the stars (1-Lowest, 5-Highest) (default {contact_data['stars']}): "
        stars = Model.validationPositive("stars", messageStars, contact_data)

        while stars < 1 or 5 < stars:
            print("Please enter a number between 1 and 5.")
            stars = Model.validationPositive("stars", messageStars, contact_data)
            
        updateContact['stars'] = stars

        isArchivedMessage = f"Enter if you want archived the review (default {contact_data['is_archived']}): "
        isArchived = Model.validationOption("is_archived", isArchivedMessage, contact_data, optionArchived)
        
        updateContact['is_archived'] = isArchived
        
        Model.update(Contacts.table, updateContact, id)