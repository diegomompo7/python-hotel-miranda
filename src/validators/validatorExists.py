def validationExists(input, value, data):
    if value is None:
        value = ""

    if value == "" and data is not None:
        return data[input]

    return value
