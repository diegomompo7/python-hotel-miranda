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

cursorObject = mydb.cursor(dictionary=True)

def executeQuery(query, params, method):
    cursorObject.execute(query % params)

    
    if method == "GET":
        result = cursorObject.fetchall()
        return result
    
    mydb.commit()
    print(cursorObject.rowcount, "record(s) affected")
    return cursorObject.lastrowid