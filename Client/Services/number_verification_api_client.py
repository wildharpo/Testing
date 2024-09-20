import requests

class NumberVerificationApiClient:
    def __init__(self):
        self._url = 'https://apilayer.net/api/validate'
        self._access_key = 'f8bfca0f38cf122b753cc188a600f9f1'

    def get_number_is_verified_response(self, number_to_validate:int):
        # attempt to verify the number via the public API
        try:
            response = requests.get(f"{self._url}?number={number_to_validate}&access_key={self._access_key}")
            return response
        except:
            raise Exception("Unable to successfully call number verification API")