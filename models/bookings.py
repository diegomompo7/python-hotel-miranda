from models.models import *
from datetime import date

class Bookings(Model):
    json_path = 'data/booking.json'
    
    def __init__(self, id):
        self.id = id
        
    def create():
        name = input("What's your name: ")
        orderDate = date.today().isoformat()
        check_in = input("Date to entry (YYYY-MM-DD): ")
        hour_in = input("Date to entry (HH:MM): ")
        check_out = input("Date to entry (YYYY-MM-DD): ")
        hour_out = input("Date to entry (HH:MM): ")
        specialRequest = input("Enter a special request (OPTIONAL): ")
        status = "Check In"
        
        newBooking = {
            "name" : name,
            "orderDate": orderDate,
            "check_in": check_in,
            "hour_in": hour_in,
            "check_out": check_out,
            "hour_out": hour_out,
            "specialRequest": specialRequest,
            "status": status,    
        }
        
        print(newBooking)
        return newBooking
    
    def update(id):
        print(id)
        booking_data = Bookings.view(str(id))

        
        