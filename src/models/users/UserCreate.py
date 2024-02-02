from ..Model import *
from datetime import *
from ...validators.validators import *

def UserCreate(newUser):
        typeJob = ["Manager", "Recepcionist", "Cleaning Room"]
        statusUser = ["ACTIVE", "INACTIVE"]

        photoInput = "Enter your profile image: "
        newUser["photo"] = validationEmpty(photoInput, input(photoInput))

        fullNameInput = "Enter your name and surname: "
        newUser["fullName"] = validationEmpty(fullNameInput, input(fullNameInput))
        
        jobInput = f"Enter your job {typeJob}: "
        job = validationOption("job", jobInput, None, typeJob)
        newUser["job"] = job

        emailInput = "Enter your email: "
        newUser["email"] = validationEmail("email", emailInput, input(emailInput), None)

        phoneInput = "Enter your phone: "
        newUser["phone"] = validationPhone("phone", phoneInput, input(phoneInput), None)
        
        startDateInput = "Enter started date to work (YYYY-MM-DD): "
        newUser["startDate"] = validationDate('startDate', startDateInput, input(startDateInput), None)

        descriptionJobInput = "Enter the description of your job: "
        newUser["descriptionJob"] = validationEmpty(descriptionJobInput, input(descriptionJobInput))

        statusInput = f"Enter the status {statusUser}: "
        status = validationOption("status", statusInput, None, statusUser)
        newUser["status"] = status

        passwordInput = "Enter your password: "
        newUser["password"] = validationPassword("password", passwordInput, input(passwordInput), None)
        
        return newUser