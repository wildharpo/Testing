import requests
import json

class NumberVerificationApi:
    def __init__(self):
        self._url = 'https://apilayer.net/api/validate'
        self._access_key = 'f8bfca0f38cf122b753cc188a600f9f1'
    
    def number_is_verified(self, number_to_validate:int):
        # ensure that the number supplied begins with a "1" prefix. If not, append it
        if int(str(number_to_validate)[:1]) != 1:
            number_to_validate = int('1' + str(number_to_validate))

        # attempt to verify the number via the public API
        try:
            response = requests.get(f"{self._url}?number={number_to_validate}&access_key={self._access_key}")
        except:
            raise Exception("Unable to successfully call number verification API")
        
        # attempt to parse the API response into a JSON object for examination
        try:
            response_json_object = json.loads(response.text)
        except:
            raise Exception("Unable to convert API response object to JSON object")
        
        # return whether or not the number is valid, according to the value of the 'valid' field on the JSON object
        return response_json_object['valid'] == True