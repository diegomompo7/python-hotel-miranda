from .models import *
from ..validators.validatorExists import *
from ..validators.validatorPositive import *
from ..validators.validatorOptions import *
from ..validators.validatorDate import *



class Users(Model):
    table = "users"

    def __init__(self, id):
        self.id = id

    def create():
        newUser = {}
        fields = executeQuery("SHOW FIELDS FROM %s", Users.table, "GET")
        for i in range(1, len(fields)):
            newUser[fields[i]["Field"]] = ""

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
        newUser["startDate"] = validationDate('startDate', startDateMessage, None)

        descriptionJob = input("Enter the description of your job: ")
        newUser["descriptionJob"] = descriptionJob

        statusMessage = f"Enter the status {statusUser}: "
        status = validationOption("status", statusMessage, None, statusUser)
        newUser["status"] = status

        password = input("Enter your password: ")
        newUser["password"] = password

        Model.create(Users.table, newUser)

    def update(id):
        user_data = Users.view(str(id))
        updateUser = user_data

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

        Model.update(Users.table, updateUser, id)
