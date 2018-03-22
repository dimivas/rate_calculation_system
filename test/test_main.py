import unittest

import rate_calculation_system


class RateCalculationSystemTestSuite(unittest.TestCase):

    def test_format_report(self):
        expected_results = ["Requested amount: GBP 1000",
                            "Rate: 12.3%",
                            "Monthly repayment: GBP 123.46",
                            "Total repayment: GBP 1234.57"]
        report = rate_calculation_system._format_report(1000, 0.123456789,
                                                        123.456789, 1234.56789)
        [self.assertEqual(expected, reported) for expected, reported in zip(expected_results, report)]

    def test_get_args(self):
        params = ["market_file", "1000", "48"]
        user_args = rate_calculation_system._get_args(params)
        self.assertEqual(params[0], user_args.market_file)
        self.assertEqual(int(params[1]), user_args.loan_amount)
        self.assertEqual(int(params[2]), user_args.duration)

    def test_get_args_default_duration(self):
        params = ["market_file", "2000"]
        user_args = rate_calculation_system._get_args(params)
        self.assertEqual(36, user_args.duration)
