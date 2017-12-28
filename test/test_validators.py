import unittest
from argparse import ArgumentTypeError

from validators import validate_header, validate_loan_amount, validate_lenders_amount


class ValidateLoanAmountTestSuite(unittest.TestCase):

    def test_upper_bound(self):
        with self.assertRaises(ArgumentTypeError):
            validate_loan_amount(1000000)

    def test_lower_bound(self):
        with self.assertRaises(ArgumentTypeError):
            validate_loan_amount(1)

    def test_valid_amount(self):
        self.assertEqual(validate_loan_amount("10000"), 10000)


class ValidateLendersAmountTestSuite(unittest.TestCase):

    def test_lower_bound(self):
        with self.assertRaises(ValueError):
            validate_lenders_amount(-1)

    def test_valid_amount(self):
        validate_lenders_amount(1000)


class ValidateHeaderTestSuite(unittest.TestCase):

    def test_valid_header(self):
        validate_header(('Lender', 'Rate', 'Available'), ";")

    def test_invalid_header(self):
        with self.assertRaises(ValueError):
            validate_header(('Lender', 'Rate', 'Unknown', 'Available'), ",")
