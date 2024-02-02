from ..Model import *
from datetime import *
from ...validators.validators import *

def UserCreate(newUser):
        typeJob = ["Manager", "Recepcionist", "Cleaning Room"]
        statusUser = ["ACTIVE", "INACTIVE"]

        photo = input("Enter your profile image: ")
        newUser["photo"] = photo

        fullName = input("Enter your name and surname: ")
        newUser["fullName"] = fullName

        jobMessage = f"Enter your job {typeJob}: "
        job = validationOption("job", jobMessage, None, typeJob)
        newUser["job"] = job

        email = input("Enter your email: ")
        newUser["email"] = email

        phone = input("Enter your phone: ")
        newUser["phone"] = phone

        startDateMessage = "Enter started date to work (YYYY-MM-DD): "
        newUser["startDate"] = validationDate('startDate', startDateMessage, input(startDateMessage), None)

        descriptionJob = input("Enter the description of your job: ")
        newUser["descriptionJob"] = descriptionJob

        statusMessage = f"Enter the status {statusUser}: "
        status = validationOption("status", statusMessage, None, statusUser)
        newUser["status"] = status

        password = input("Enter your password: ")
        newUser["password"] = password