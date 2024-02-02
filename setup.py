from src.db.sql import mydb, cursorObject

sqlFile = "src/scripts/HotelMiranda.sql"

try:
    with open(sqlFile) as sql:
       script = sql.read()
       
    commands = script.split(";")
       
    for command in commands:
        if command.strip():
               cursorObject.execute(command)
               
    mydb.commit()
       
except Exception as e:
    print(f'Error: {e}')
finally:
    if cursorObject:
        cursorObject.close()


