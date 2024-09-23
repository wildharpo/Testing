# import path to the Python modules in our subfolders. There are other (better) ways to do this, but for the 
# sake of simplicity we'll use this for demonstration purposes
import sys, os
sys.path.append(os.path.join(sys.path[0], 'Services'))
sys.path.append(os.path.join(sys.path[0], 'Helpers'))
sys.path.append(os.path.join(sys.path[0], 'DataAccess'))

# import our number formatter and number verification API libraries
from number_verification_api import *
from number_formatter import *
from volunteer_repo import *

# use the '__name__ == "__main__"' sanity check to prevent this piece of logic from accidentally running if 
# this library is used in an import statement elsewhere in the code, yet not meant to be the entry point
if __name__ == "__main__":
    # ask user to enter a phone number
    print("Please enter a phone number to verify: ")
    phone_number_str = input()

    # format the entered phone number
    print("Formatting number...")
    phone_number = get_formatted_number(phone_number_str)

    # see if number already exists in database
    print("Seeing if number already exists in database...")
    repo = VolunteerRepo()
    existing_customer = repo.get_volunteer_by_phone_number(phone_number)
    if existing_customer != None:
        print(f"This customer already exists! Phone number {existing_customer.phone_number} belongs to '{existing_customer.first_name} {existing_customer.last_name}'")
    else:
        # verify that the phone number exists using the public API
        print("Customer does not exist in database. Verifying provided number...")
        num_verification_api = NumberVerificationApi()
        number_is_verified = num_verification_api.number_is_verified(phone_number)

        if number_is_verified:
            # ask user to enter first name, last name, and email associated with that phone number
            print("Phone number is valid, please enter additional fields.")
            print("First Name: ")
            first_name = input()
            print("Last Name: ")
            last_name = input()
            print("Email: ")
            email = input()

            # save new user to database
            print("Saving new user to database...")
            volunteer = Volunteer(first_name, last_name, phone_number, email)
            repo.save_volunteer(volunteer)
            print("User saved!")
        else:
            print("Provided number was invalid.")
