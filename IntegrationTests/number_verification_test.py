import unittest
import sys, os
sys.path.append(os.path.join(sys.path[0], '../../Client/Helpers'))
sys.path.append(os.path.join(sys.path[0], '../../Client/Services'))
from number_formatter import *
from number_verification_api import *

class NumberVerificationTest(unittest.TestCase):
    def VerifyNumberFormattedAndVerified(self):
        formatted_number = get_formatted_number('1-417-439-7795')
        num_verification_api = NumberVerificationApi()
        verification_result = num_verification_api.number_is_verified(formatted_number)
        self.assertEqual(14174397795,verification_result)