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
