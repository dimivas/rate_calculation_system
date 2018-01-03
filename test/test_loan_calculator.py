import unittest

import loan_calculator
import numpy
import uuid

class LoanCalculatorTestSuite(unittest.TestCase):

    def _get_sample_market_data(self):
        market_data = numpy.array(((uuid.uuid4(), 0.12, 1000),
                                   (uuid.uuid4(), 0.20, 500),
                                   (uuid.uuid4(), 0.27, 750)))
        return market_data

    def test_calculate_monthly_repayment(self):
        monthly_repayment = loan_calculator._calculate_monthly_repayment(5000, 0.12, 36)
        self.assertEqual(monthly_repayment, 164.61038604391155)

    def test_calculate_total_repayment(self):
        total_repayment = loan_calculator._calculate_total_repayment(164.61038604391155, 36)
        self.assertEqual(total_repayment, 5925.973897580816)

    def test_calculate_contribution_rate(self):
        row = numpy.array((0.123, 1000))
        contr_rate = loan_calculator._calculate_contribution_rate(row, 5000)
        self.assertEqual(contr_rate, 0.0246)

    def test_calculate_loan_invalid_amount(self):
        market_data = self._get_sample_market_data()
        with self.assertRaises(Exception):
            loan_calculator.calculate_loan(market_data, 10000, 36)

    def test_calculate_loan_valid_amount(self):
        market_data = self._get_sample_market_data()
        rate, monthly_repayment, total_repayment = loan_calculator.calculate_loan(market_data, 2000, 12)
        self.assertEqual(rate, 0.1775)
        self.assertEqual(monthly_repayment, 181.88893002366027)
        self.assertEqual(total_repayment, 2182.6671602839233)
