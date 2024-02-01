from abc import ABC, abstractmethod
import json
from datetime import date
from sql import executeQuery


class Model(ABC):
    table = None

    @classmethod
    def list(cls):
        result = executeQuery("SELECT * FROM %s ;", cls.table, "GET")
        for data in result:
            print(data)
        

    @classmethod
    def view(cls, id):
        result = executeQuery("SELECT * FROM %s WHERE id=%s;", (cls.table, id), "GET")
            
        for data in result:
            print(data)
            return data
        print(f"id not found")

    @classmethod
    def delete(cls, id):
        result = executeQuery("DELETE FROM %s WHERE id = %s", (cls.table, id), "DELETE")
        if result == 0:
            print("id not found")

    @classmethod
    def create(cls, table, data):
        lastId = executeQuery("INSERT INTO %s (%s) VALUES %s;", (table, ",".join(list(data.keys())), tuple(data.values())), "POST")
        print(type(lastId))
        return lastId
    
    @classmethod
    def update(self, table, data, id):
        setColumns = []
        for key, value in data.items():
           setColumns.append(f"{key} = '{value}'")
        
        executeQuery("UPDATE %s SET %s WHERE id=%s", (table, ",".join(setColumns), id), "PATCH")
        

    def validationExists(input, value, data):
        if value is None:
            value = ""
            
        if value == "" and data is not None:
            return data[input]

        return value

    def validationOption(inputColumn, inputMessage, data, options):
        try:

            if inputColumn == 'room_id':
                optionInput = Model.validationPositive('room_id', inputMessage, data)
            else:
                optionInput = input(inputMessage)

            checkOption = Model.validationExists(inputColumn, optionInput, data)

            if options.count(checkOption) != 0:
                return checkOption

            print(f"Please enter a valid option between this {options}.")
            return Model.validationOption(inputColumn, inputMessage, data, options)

        except ValueError:
                print(f"Please enter a valid option between this {options}.")
                return Model.validationOption(inputColumn, inputMessage, data, options)

    def validationPositive(inputColumn, inputMessage, data):
        try:
            if data is not None:
                numberInput = input(inputMessage)
            else:
                numberInput = int(input(inputMessage))

            checkNumber = Model.validationExists(inputColumn, numberInput, data)

            if type(checkNumber) == list:
                return len(checkNumber)

            numberInput = int(checkNumber)

            if numberInput > 0:
                return numberInput
            else:
                print("Please enter a positive integer.")
                return Model.validationPositive(inputColumn, inputMessage, data)
        except ValueError:
                print("Please enter a valid integer.")
                return Model.validationPositive(inputColumn, inputMessage, data)
            