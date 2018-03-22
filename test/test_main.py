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