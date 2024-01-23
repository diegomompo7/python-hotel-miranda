from models.models import *
from datetime import date

class Contacts(Model):
    json_path = 'data/contact.json'
    
    def __init__(self, id):
        self.id = id
        
    def create():
        userImg = input("Enter your image: ")
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone: ")
        date = input("Enter date when wrote the review (YYYY-MM-DD): ")
        subject= input("Enter the subject of review: ")
        message = input("Enter your message: ")
        stars= int(input("Enter the stars (1-Lowest, 5-Highest): "))
        is_archived = False
        
        newContact = {
            "userImg": userImg,
            "name" : name,
            "surname": surname,
            "email": email,
            "phone": phone,
            "date": date,
            "subject": subject,
            "message": message,
            "stars": stars,
            "is_archived": is_archived
        }
        
        print(newContact)
        return newContact
    
    def update(id):
        contact_data = Contacts.view(str(id))
        
        userImg = input(f"Enter your image (default {contact_data.get('userImg')}): ") or contact_data.get("userImg")
        name = input(f"Enter your name (default {contact_data.get('name')}): ") or contact_data.get("name")
        surname = input(f"Enter your surname (default {contact_data.get('surname')}): ") or contact_data.get("surname")
        email = input(f"Enter your email (default {contact_data.get('email')}): ") or contact_data.get("email")
        phone = input(f"Enter your phone (default {contact_data.get('phone')}): ") or contact_data.get("phone")
        date = input(f"Enter date when wrote the review (YYYY-MM-DD) (default {contact_data.get('date')}): ") or contact_data.get("date")
        subject= input(f"Enter the subject of review (default {contact_data.get('subject')}): ") or contact_data.get("subject")
        message = input(f"Enter your message (default {contact_data.get('message')}): ") or contact_data.get("message")
        stars= int(input(f"Enter the stars (1-Lowest, 5-Highest) (default {contact_data.get('stars')}): ") or contact_data.get("stars"))
        is_archived = input(f"Enter if yo want archived the review (default {contact_data.get('is_archived')}): ") or contact_data.get("is_archived")
        

        updateContact = {
            "userImg": userImg,
            "name" : name,
            "surname": surname,
            "email": email,
            "phone": phone,
            "date": date,
            "subject": subject,
            "message": message,
            "stars": stars,
            "is_archived": is_archived   
        }
        
        print(updateContact)
        return updateContact
        

        
        