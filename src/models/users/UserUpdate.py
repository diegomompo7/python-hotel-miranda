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

        jobMessage = f"Enter your job {typeJob} (default {user_data.get('job')}): "
        job = validationOption("job", jobMessage, user_data, typeJob)
        updateUser["job"] = job

        email = input(f"Enter your email (default {user_data.get('email')}): ")
        updateUser["email"] = validationExists("email", email, user_data)

        phone = input(f"Enter your phone (default {user_data.get('phone')}): ")
        updateUser["phone"] = validationExists("phone", phone, user_data)

        startDateMessage = f"Enter started date to work (YYYY-MM-DD) (default {user_data.get('startDate')}): "
        updateUser["startDate"] = validationDate('startDate', startDateMessage, user_data)


        descriptionJob = input(
            f"Enter the description of your job (default {user_data.get('descriptionJob')}): "
        )
        updateUser["descriptionJob"] = validationExists(
            "descriptionJob", descriptionJob, user_data
        )

        statusMessage = (
            f"Enter the status {statusUser} (default {user_data.get('status')}): "
        )
        status = validationOption("status", statusMessage, user_data, statusUser)
        updateUser["status"] = status

        password = input(f"Enter your password: ")
        updateUser["password"] = validationExists("password", password, user_data)
        
        return updateUser

        