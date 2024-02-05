from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

    
class Contact(models.Model):
    id = models.AutoField(primary_key=True)    
    userImg = models.URLField(("userImg"), max_length=200)
    name = models.CharField(max_length = 255)
    surname = models.CharField(max_length = 255)
    email = models.EmailField(("Email"), max_length=255)
    phone = models.CharField(max_length = 9, validators=[
        RegexValidator(
                regex=r'^(0|91)?[6-9][0-9]{8}',
                message="Enter a valid format phone number",
                code="invalid_registration",
        )
    ])
    date = models.DateField()
    subject = models.CharField(max_length = 100)
    message = models.TextField(max_length = 255)
    stars = models.IntegerField(validators = [
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    is_archived = models.BooleanField(default = False)


