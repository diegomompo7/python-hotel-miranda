import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
    host="localhost",
    user= os.getenv('API_USERNAME'),
    password= os.getenv('API_PASSWORD'),
    database=os.getenv('API_DATABASE')
)

cursorObject = mydb.cursor()

def executeQuery(query, params):
    cursorObject.execute(query % params)
    
    result = cursorObject.fetchall()

    return result