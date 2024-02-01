from ..validators.validatorExists import *
from datetime import datetime

def validationDate(inputColumn, inputMessage, data):
    try:
        dateInput = input(inputMessage)

        checkDate = validationExists(inputColumn, dateInput, data)
        
        formatDate = datetime.strptime(checkDate, '%Y-%m-%d').strftime('%Y-%m-%d')
        
        if inputColumn == 'check_out':
            formatDate = validationCheckOut(inputColumn, inputMessage, data, formatDate, data['check_in'])
            
        return formatDate
        
    except ValueError:
        print("Insert a valid format Date")
        return validationDate(inputColumn, inputMessage, data)

def validationCheckOut(inputColumn, inputMessage, data, checkOutDate, checkInDate):
    print(checkOutDate, checkInDate)
    if checkOutDate < checkInDate:
        print("Insert a date Out higher date In")
        return validationDate(inputColumn, inputMessage, data)
    
    return checkOutDate