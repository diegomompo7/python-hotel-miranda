from ..validators.validatorExists import *

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
