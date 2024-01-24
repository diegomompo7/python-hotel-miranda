from models.models import *
from datetime import date

#'id': 1,
#'photo': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
# 'fullName': 'Diego Mompo',
# 'job': 'Manager',
# 'email': 'diego@gmail.com',
# 'phone': '+34 788128729',
# 'startDate': '2023-02-03',
# 'descriptionJob': 'Responsable de la gestión operativa del hotel. Toma decisiones estratégicas y coordina las actividades de los diferentes departamentos.',
# 'status': 'ACTIVE',
# 'password': 'diego23'}


class Users(Model):
    json_path = "data/users.json"

    def __init__(self, id):
        self.id = id

    def create():
        photo = input("Enter your profile image: ")
        fullName = input("Enter your name and surname: ")
        job = input("Enter your job (Manger, Recepcionist, Cleaning Room): ")
        email = input("Enter your email: ")
        phone = input("Enter your phone: ")
        startDate = input("Enter started date to work (YYYY-MM-DD): ")
        descriptionJob = input("Enter the description of your job: ")
        status = input("Enter the status (ACTIVE, INACTIVE): ")
        password = input("Enter your password: ")

        newUser = {
            "photo": photo,
            "fullName": fullName,
            "job": job,
            "email": email,
            "phone": phone,
            "startDate": startDate,
            "descriptionJob": descriptionJob,
            "status": status,
            "password": password,
        }

        print(newUser)
        return newUser

    def update(id):
        user_data = Users.view(str(id))

        photo = input(
            f"Enter your profile image (default {user_data.get('photo')}): "
        ) or user_data.get("photo")
        fullName = input(
            f"Enter your name and surname (default {user_data.get('fullName')}): "
        ) or user_data.get("fullName")
        job = input(
            f"Enter your job (Manger, Recepcionist, Cleaning Room) (default {user_data.get('job')}): "
        ) or user_data.get("job")
        email = input(
            f"Enter your email (default {user_data.get('email')}): "
        ) or user_data.get("email")
        phone = input(
            f"Enter your phone (default {user_data.get('phone')}): "
        ) or user_data.get("phone")
        startDate = input(
            f"Enter started date to work (YYYY-MM-DD) (default {user_data.get('startDate')}): "
        ) or user_data.get("startDate")
        descriptionJob = input(
            f"Enter the description of your job (default {user_data.get('descriptionJob')}): "
        ) or user_data.get("descriptionJob")
        status = input(
            f"Enter the status (ACTIVE, INACTIVE) (default {user_data.get('status')}): "
        ) or user_data.get("status")
        password = input(f"Enter your password: ") or user_data.get("password")

        updateUser = {
            "photo": photo,
            "fullName": fullName,
            "job": job,
            "email": email,
            "phone": phone,
            "startDate": startDate,
            "descriptionJob": descriptionJob,
            "status": status,
            "password": password,
        }

        print(updateUser)
        return updateUser
