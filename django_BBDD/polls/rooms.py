from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class RoomType(models.TextChoices):
    SINGLE_BED = "Single Bed", "Single Bed"
    DOUBLE_BED = "Double Bed", "Double Bed"
    DOUBLE_SUPERIOR = "Double Superior", "Double Superior"
    SUITE = "Suite"
    
class OfferRoom(models.TextChoices):
    YES = "YES", "YES"
    NO = "NO", "NO"
     
class StatusRoom(models.TextChoices):
    AVAILABLE = "Available", "Available"
    BOOKED = "Booked", "Booked"
    
class Room(models.Model):
    id = models.AutoField(primary_key=True)
    photos= models.JSONField()
    roomType = models.CharField(max_length = 20, choices = RoomType.choices)
    roomNumber = models.CharField(max_length = 50)
    description = models.TextField(max_length = 255)
    offer = models.CharField(max_length = 3, choices = OfferRoom.choices)
    priceNight = models.DecimalField(max_digits=10, decimal_places=2, validators = [
        MinValueValidator(50.00),
        MaxValueValidator(200.00)
    ])
    discount = models.PositiveIntegerField(validators = [
        MinValueValidator(0),
        MaxValueValidator(50)
    ])
    cancellation = models.TextField(max_length = 255)
    status = models.CharField(max_length = 20, choices = StatusRoom.choices)