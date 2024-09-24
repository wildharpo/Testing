import unittest
import sys, os
sys.path.append(os.path.join(sys.path[0], '../../../Client/Helpers'))

from number_formatter import *

class NumberFormatterFixture(unittest.TestCase):
    def test_hyphens_are_removed(self):
        self.assertEqual(14174397795,get_formatted_number('417-439-7795'))

    def test_number_beginning_with_one_doesnt_receive_duplicate_one(self):
        self.assertEqual(14174397795,get_formatted_number('1-417-439-7795'))

    def test_nonnumeric_characters_are_removed(self):
        self.assertEqual(14174397795,get_formatted_number('4sd17g43hf97p79d5'))

    def test_short_number_raises_exception(self):
        with self.assertRaises(ValueError):
            get_formatted_number('1234')

if __name__ == '__main__':
    # if this file is launched directly, then run all unit tests included in it
    unittest.main()