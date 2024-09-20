import re
import math

def get_formatted_number(provided_number:str):
    # remove all non-numeric characters from the provided number value using regular expressions.
    formatted_number:int = int(re.sub("[^0-9]", "", provided_number))
    
    # as the shortest international phone numbers available use seven digits, ensure that the 
    # provided number is at least that long. If it is not, throw an exception.
    num_digits:int = int(math.log10(formatted_number))+1
    if num_digits < 7:
        raise ValueError('A valid number must have at least seven digits')

    # ensure that the number supplied begins with a "1" prefix. If not, prepend it.
    if int(str(formatted_number)[:1]) != 1:
        formatted_number = int('1' + str(formatted_number))

    return formatted_number