from datetime import datetime, date

def validationDate(inputColumn, inputMessage, inputValue, data):
    try:
        checkDate = validationExists(inputColumn, inputValue, data)
        
        print(type(checkDate).__name__)
        
        if type(checkDate).__name__ == 'date':
            print("True")
            checkDate = checkDate.isoformat()
            
        formatDate = datetime.strptime(checkDate, '%Y-%m-%d').strftime('%Y-%m-%d')
        
        if inputColumn == 'check_out':
            formatDate = validationCheckOut(inputColumn, inputMessage, data, formatDate, data['check_in'])
            
        return formatDate
        
    except ValueError:
        print("Insert a valid format Date")
        return validationDate(inputColumn, inputMessage, input(inputMessage), data)
    
def validationTime(inputColumn, inputMessage, inputValue, data):
    try:
        checkTime = validationExists(inputColumn, inputValue, data)
        
        print(type(checkTime).__name__)
        
        if type(checkTime).__name__ == 'timedelta':
            hours = int(checkTime.total_seconds() // 3600)
            minutes = int((checkTime.total_seconds() % 3600) // 60)
            checkTime = f"{hours}:{minutes}"
            
        print(checkTime)
            
        formatTime = datetime.strptime(checkTime, '%H:%M').strftime('%H:%M')
        
        if inputColumn == 'check_out':
            formatTime = validationCheckOut(inputColumn, inputMessage, data, formatTime, data['check_in'])
            
        return formatTime
        
    except ValueError:
        print("Insert a valid format Time")
        return validationTime(inputColumn, inputMessage, input(inputMessage), data)

def validationCheckOut(inputColumn, inputMessage, data, checkOutDate, checkInDate):
    if checkOutDate < checkInDate:
        print("Insert a date Out higher date In")
        return validationDate(inputColumn, inputMessage, input(inputMessage), data)
    
    return checkOutDate

def validationExists(input, value, data):
    if value is None:
        value = ""

    if value == "" and data is not None:
        return data[input]

    return value

def validationOption(inputColumn, inputMessage, data, options):
    try:
        if inputColumn == "room_id":
            optionInput = validationPositive("room_id", inputMessage, data)
        else:
            optionInput = input(inputMessage)

        checkOption = validationExists(inputColumn, optionInput, data)

        if options.count(checkOption) != 0:
            return checkOption

        print(f"Please enter a valid option between this {options}.")
        return validationOption(inputColumn, inputMessage, data, options)

    except ValueError:
        print(f"Please enter a valid option between this {options}.")
        return validationOption(inputColumn, inputMessage, data, options)

def validationPositive(inputColumn, inputMessage, data):
    try:
        if data is not None:
            numberInput = input(inputMessage)
        else:
            numberInput = int(input(inputMessage))

        checkNumber = validationExists(inputColumn, numberInput, data)

        if type(checkNumber) == list:
            return len(checkNumber)

        numberInput = int(checkNumber)

        if numberInput > 0:
            return numberInput
        else:
            print("Please enter a positive integer.")
            return validationPositive(inputColumn, inputMessage, data)
    except ValueError:
        print("Please enter a valid integer.")
        return validationPositive(inputColumn, inputMessage, data)
