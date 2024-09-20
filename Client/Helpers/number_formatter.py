import re

def get_formatted_number(provided_number:str):
    # remove all non-numeric characters from the provided number value using regular expressions
    formatted_number = int(re.sub("[^0-9]", "", provided_number))

    # ensure that the number supplied begins with a "1" prefix. If not, prepend it
    if int(str(formatted_number)[:1]) != 1:
        formatted_number = int('1' + str(formatted_number))

    return formatted_number