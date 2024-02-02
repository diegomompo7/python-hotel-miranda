from ..Model import *
from datetime import *
from ...validators.validators import *

def UserUpdate(user_data, updateUser, roomId):
        typeJob = ["Manager", "Recepcionist", "Cleaning Room"]
        statusUser = ["ACTIVE", "INACTIVE"]

        photo = input(f"Enter your profile image (default {user_data.get('photo')}): ")
        updateUser["photo"] = validationExists("photo", photo, user_data)

        fullName = input(
            f"Enter your name and surname (default {user_data.get('fullName')}): "
        )
        updateUser["fullName"] = validationExists("fullName", fullName, user_data)

        jobInput = f"Enter your job {typeJob} (default {user_data.get('job')}): "
        job = validationOption("job", jobInput, user_data, typeJob)
        updateUser["job"] = job

        emailInput = f"Enter your email (default {user_data['email']}): "
        updateUser["email"] = validationEmail("email", emailInput, input(emailInput), user_data)
        
        phoneInput = f"Enter your phone (default {user_data['phone']}): "
        updateUser["phone"] = validationPhone("phone", phoneInput, input(phoneInput), user_data)

        startDateInput = f"Enter started date to work (YYYY-MM-DD) (default {user_data.get('startDate')}): "
        updateUser["startDate"] = validationDate('startDate', startDateInput, input(startDateInput), user_data)


        descriptionJob = input(
            f"Enter the description of your job (default {user_data.get('descriptionJob')}): "
        )
        updateUser["descriptionJob"] = validationExists(
            "descriptionJob", descriptionJob, user_data
        )

        statusInput = (
            f"Enter the status {statusUser} (default {user_data.get('status')}): "
        )
        status = validationOption("status", statusInput, user_data, statusUser)
        updateUser["status"] = status

        passwordInput = f"Enter your password: "
        updateUser["password"] = validationPassword("password", passwordInput, input(passwordInput), user_data)
        
        return updateUser

        