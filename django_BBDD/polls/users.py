from django.db import models
from django.core.validators import RegexValidator

class JobUser(models.TextChoices):
    MANAGER = "Manager", "Manager"
    RECEPTIONIST = "Receptionist", "Receptionist"
    CLEANING_ROOM = "Cleaning Room", "Cleaning Room"
    
class StatusUser(models.TextChoices):
    ACTIVE = "ACTIVE", "ACTIVE"
    INACTIVE = "INACTIVE", "INACTIVE"
    

class User(models.Model):
    id = models.AutoField(primary_key=True)
    photo = models.URLField(("photo"), max_length=200)
    fullName = models.CharField(max_length = 255)
    job = models.CharField(max_length = 100, choices = JobUser.choices)
    email = models.EmailField(("Email"), max_length=255, unique=True)
    phone = models.CharField(max_length = 9, validators=[
        RegexValidator(
                regex=r'^(0|91)?[6-9][0-9]{8}',
                message="Enter a valid format phone number",
                code="invalid_registration",
        )
    ], unique = True)
    startDate = models.DateField(auto_now = True)
    descriptionJob = models.TextField(max_length = 255)
    status = models.CharField(max_length = 10, choices = StatusUser.choices, default="ACTIVE")
    password = models.CharField(max_length = 20, validators=[
        RegexValidator(
                regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}',
                message="Enter a valid format password",
                code="invalid_registration",
        )
    ])


