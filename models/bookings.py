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
        booking_data = Bookings.view(str(id))
        
        name = input(f"What's your name (default {booking_data.get('name')}): ") or booking_data.get("name")
        check_in = input(f"Date to entry (YYYY-MM-DD) (default {booking_data.get('check_in')}): ") or booking_data.get("check_in")
        hour_in = input(f"Date to entry (HH:MM)  (default {booking_data.get('hour_in')}): ") or booking_data.get("hour_in")
        check_out = input(f"Date to entry (YYYY-MM-DD)  (default {booking_data.get('check_out')}): ") or booking_data.get("check_out")
        hour_out = input(f"Date to entry (HH:MM) (default {booking_data.get('hour_out')}): ") or booking_data.get("hour_out")
        specialRequest = input(f"Enter a special request (OPTIONAL) (default {booking_data.get('specialRequest')}): ") or booking_data.get("specialRequest")
        status = input(f"Enter a status (Check In, Check Out, In Progress) (default {booking_data.get('status')}): ") or booking_data.get("status")

        updateBooking = {
            "name" : name,
            "check_in": check_in,
            "hour_in": hour_in,
            "check_out": check_out,
            "hour_out": hour_out,
            "specialRequest": specialRequest,
            "status": status,    
        }
        
        print(updateBooking)
        return updateBooking
        

        
        