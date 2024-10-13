import unittest
from requests import *
from unittest.mock import Mock
import sys, os
sys.path.append(os.path.join(sys.path[0], '../../../Client/Services'))

from number_verification_api import *
from number_verification_api_client import *

class NumberVerificationApiFixture(unittest.TestCase):
    # verify that an exception thrown by the NumberVerificationApiClient is handled
    def test_api_call_exception_is_handled(self):
        # create a mock of our NumberVerificationApiClient class as we don't want to use a functional instance
        mock_number_verification_api_client = Mock()
        # force its get_number_is_verified_response to raise an exception in our mock object
        mock_number_verification_api_client.get_number_is_verified_response.side_effect = Exception('Oops!')
        # assert that the exception is indeed raised when the number_is_verified function is called
        with self.assertRaises(Exception):
            NumberVerificationApi(mock_number_verification_api_client).number_is_verified('417-820-1234')

    # verify that invalid JSON returned by the NumberVerificationApiClient response object is handled
    def test_invalid_json_response_is_handled(self):
        # create a mock of our NumberVerificationApiClient class as we don't want to use a functional instance
        mock_number_verification_api_client = Mock()
        # create a mock Response object that our mock NumberVerificationApiClient should return when get_number_is_verified_response is called
        mock_response = Mock()
        # have our fake response text return invalid JSON data as a string
        mock_response.text = '{"valid"": true,"number": "14158586273","local_format": "4158586273","international_format": "+14158586273","country_prefix": "+1","country_code": "US","country_name": "United States of America","location": "Novato","carrier": "AT&T Mobility LLC","line_type": "mobile"}'
        # return the mock response when get_number_is_verified_response is called
        mock_number_verification_api_client.get_number_is_verified_response.return_value = mock_response
        # assert that the exception is indeed raised when the above invalid JSON is parsed (or rather attempted to be parsed)
        with self.assertRaises(Exception):
            NumberVerificationApi(mock_number_verification_api_client).number_is_verified('417-820-1234')

    # verify that a valid number passed to the NumberVerificationApi number_is_verified method returns "True"
    def test_valid_number_returns_true(self):
        # create a mock of our NumberVerificationApiClient class as we don't want to use a functional instance
        mock_number_verification_api_client = Mock()
        # create a mock Response object that our mock NumberVerificationApiClient should return when get_number_is_verified_response is called
        mock_response = Mock()
        # have our fake response text for this object have valid = true in its data
        mock_response.text = '{"valid": true,"number": "14158586273","local_format": "4158586273","international_format": "+14158586273","country_prefix": "+1","country_code": "US","country_name": "United States of America","location": "Novato","carrier": "AT&T Mobility LLC","line_type": "mobile"}'
        # return the mock response when get_number_is_verified_response is called
        mock_number_verification_api_client.get_number_is_verified_response.return_value = mock_response
        # create a NumberVerificationApi instance with our mock NumberVerificationApiClient object passed to it
        number_verification_api = NumberVerificationApi(mock_number_verification_api_client)
        # assert that a valid number passed returns "True"
        self.assertEqual(True,number_verification_api.number_is_verified('4178201234'))
    
    # verify that an invalid number passed to the NumberVerificationApi number_is_verified method returns "False"
    def test_invalid_number_returns_false(self):
        # create a mock of our NumberVerificationApiClient class as we don't want to use a functional instance
        mock_number_verification_api_client = Mock()
        # create a mock Response object that our mock NumberVerificationApiClient should return when get_number_is_verified_response is called
        mock_response = Mock()
        # 
        mock_response.text = '{"valid": false,"number": "","local_format": "","international_format": "","country_prefix": "","country_code": "","country_name": "","location": "","carrier": "","line_type": ""}'
        # return the mock response when get_number_is_verified_response is called
        mock_number_verification_api_client.get_number_is_verified_response.return_value = mock_response
        # create a NumberVerificationApi instance with our mock NumberVerificationApiClient object passed to it
        number_verification_api = NumberVerificationApi(mock_number_verification_api_client)
        # assert that an invalid number passed returns "False"
        self.assertEqual(False,number_verification_api.number_is_verified('9999999999'))       

if __name__ == '__main__':
    # if this file is launched directly, then run all unit tests included in it
    unittest.main()
