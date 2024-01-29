from models.models import *

class Users(Model):
    table = "users"

    def __init__(self, id):
        self.id = id

    def create():
        
        typeJob = ["Manager", "Recepcionist", "Cleaning Room"]
        statusUser = ["ACTIVE, INACTIVE"]
        
        photo = input("Enter your profile image: ")
        fullName = input("Enter your name and surname: ")
        
        jobMessage = f"Enter your job {typeJob}: "
        job = Model.validationOption("job", jobMessage, None, typeJob)
        
        email = input("Enter your email: ")
        phone = input("Enter your phone: ")
        startDate = input("Enter started date to work (YYYY-MM-DD): ")
        descriptionJob = input("Enter the description of your job: ")
        
        statusMessage = f"Enter the status {statusUser}: "
        status = Model.validationOption("status", statusMessage, None, statusUser)
        
        password = input("Enter your password: ")

        Model.user(photo, fullName, job, email, phone, startDate, descriptionJob, status, password, None)

    def update(id):
        user_data = Users.view(str(id))
        typeJob = ["Manager", "Recepcionist", "Cleaning Room"]
        statusUser = ["ACTIVE", "INACTIVE"]

        photo = input(
            f"Enter your profile image (default {user_data.get('photo')}): "
        )
        fullName = input(
            f"Enter your name and surname (default {user_data.get('fullName')}): "
        )
        
        jobMessage = f"Enter your job {typeJob} (default {user_data.get('job')}): "
        job = Model.validationOption("job", jobMessage, user_data, typeJob)


        email = input(
            f"Enter your email (default {user_data.get('email')}): "
        )
        phone = input(
            f"Enter your phone (default {user_data.get('phone')}): "
        )
        startDate = input(
            f"Enter started date to work (YYYY-MM-DD) (default {user_data.get('startDate')}): "
        )
        descriptionJob = input(
            f"Enter the description of your job (default {user_data.get('descriptionJob')}): "
        )
        statusMessage = f"Enter the status {statusUser} (default {user_data.get('status')}): "
        status = Model.validationOption("status", statusMessage, user_data, statusUser)
        
        password = input(f"Enter your password: ")

        Model.user(photo, fullName, job, email, phone, startDate, descriptionJob, status, password, user_data)