# import path to the Python modules in our subfolders. There are other (better) ways to do this, but for the 
# sake of simplicity we'll use this for demonstration purposes
import sys
sys.path.insert(1, '/Users/vbnetl8r6062/source/Testing/Client/Services')
sys.path.insert(1, '/Users/vbnetl8r6062/source/Testing/Client/Helpers')

# import our number formatter and number verification API libraries
from number_verification_api import *
from number_formatter import *

# use the '__name__ == "__main__"' sanity check to prevent this piece of logic from accidentally running if 
# this library is used in an import statement elsewhere in the code, yet not meant to be the entry point
if __name__ == "__main__":
    # ask user to enter a phone number
    print("Please enter a phone number to verify")
    phone_number_str = input()

    # format the entered phone number
    print("Formatting number...")
    phone_number = get_formatted_number(phone_number_str)

    # verify that the phone number exists using the public API
    print("Verifying number...")
    num_verification_api = NumberVerificationApi()
    number_is_verified = num_verification_api.number_is_verified(phone_number)