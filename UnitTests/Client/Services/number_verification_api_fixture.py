import unittest
from requests import *
from unittest.mock import Mock
import sys, os
sys.path.append(os.path.join(sys.path[0], '../../../Client/Services'))

from number_verification_api import *
from number_verification_api_client import *

class NumberVerificationApiFixture(unittest.TestCase):
    def test_api_call_exception_is_handled(self):
        mock_number_verification_api_client = Mock()
        mock_number_verification_api_client.get_number_is_verified_response.side_effect = Exception('Oops!')
        with self.assertRaises(Exception):
            NumberVerificationApi(mock_number_verification_api_client).number_is_verified('417-439-7795')

    def test_invalid_json_response_is_handled(self):
        mock_number_verification_api_client = Mock()
        mock_response = Mock()
        mock_response.text = '{"valid"": true,"number": "14158586273","local_format": "4158586273","international_format": "+14158586273","country_prefix": "+1","country_code": "US","country_name": "United States of America","location": "Novato","carrier": "AT&T Mobility LLC","line_type": "mobile"}'
        mock_number_verification_api_client.get_number_is_verified_response.return_value = mock_response
        with self.assertRaises(Exception):
            NumberVerificationApi(mock_number_verification_api_client).number_is_verified('417-439-7795')

    def test_valid_number_returns_true(self):
        mock_number_verification_api_client = Mock()
        mock_response = Mock()
        mock_response.text = '{"valid": true,"number": "14158586273","local_format": "4158586273","international_format": "+14158586273","country_prefix": "+1","country_code": "US","country_name": "United States of America","location": "Novato","carrier": "AT&T Mobility LLC","line_type": "mobile"}'
        mock_number_verification_api_client.get_number_is_verified_response.return_value = mock_response
        number_verification_api = NumberVerificationApi(mock_number_verification_api_client)
        self.assertEqual(True,number_verification_api.number_is_verified('4174397795'))
    
    def test_invalid_number_returns_false(self):
        mock_number_verification_api_client = Mock()
        mock_response = Mock()
        mock_response.text = '{"valid": false,"number": "0"}'
        mock_number_verification_api_client.get_number_is_verified_response.return_value = mock_response
        number_verification_api = NumberVerificationApi(mock_number_verification_api_client)
        self.assertEqual(False,number_verification_api.number_is_verified('9999999999'))       

if __name__ == '__main__':
    unittest.main()
