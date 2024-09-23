import json
from number_verification_api_client import *

class NumberVerificationApi:
    def __init__(self):
        client = NumberVerificationApiClient()
        self._client = client
    
    def number_is_verified(self, number_to_validate:int):
        # attempt to verify the number via the public API
        try:
            response = self._client.get_number_is_verified_response(number_to_validate)
        except:
            raise Exception("Unable to successfully call number verification API")

        # attempt to parse the API response into a JSON object for examination
        try:
            response_json_object = json.loads(response.text)
        except:
            raise Exception("Unable to convert API response object to JSON object")
        
        # return whether or not the number is valid, according to the value of the 'valid' field on the JSON object
        return response_json_object['valid'] == True