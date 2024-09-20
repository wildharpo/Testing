import sys
sys.path.insert(1, '/Users/vbnetl8r6062/source/Testing/Client/Services')
sys.path.insert(1, '/Users/vbnetl8r6062/source/Testing/Client/Helpers')

from number_verification_api import *
from number_formatter import *

if __name__ == "__main__":
    print("Please enter a phone number to verify")
    phone_number_str = input()

    print("Formatting number...")
    phone_number = get_formatted_number(phone_number_str)

    print("Verifying number...")
    num_verification_api = NumberVerificationApi()
    number_is_verified = num_verification_api.number_is_verified(phone_number)