import requests
import os
from dotenv import load_dotenv

class NumberVerificationApiClient:
    def __init__(self):
        load_dotenv()
        self._url = 'https://apilayer.net/api/validate'
        self._access_key = os.getenv('NUM_VERIFIER_ACCESS_KEY')

    def get_number_is_verified_response(self, number_to_validate:int):
        # attempt to verify the number via the public API
        try:
            response = requests.get(f"{self._url}?number={number_to_validate}&access_key={self._access_key}")
            return response
        except:
            raise Exception("Unable to successfully call number verification API")