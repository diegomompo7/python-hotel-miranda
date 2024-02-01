from ..validators.validatorExists import *
from ..validators.validatorPositive import *

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
