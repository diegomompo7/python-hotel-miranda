from django.contrib import admin
from .bookings import Booking
from .rooms import Room
from .contacts import Contact
from .users import User

# Register your models here.
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Room)
admin.site.register(Booking)