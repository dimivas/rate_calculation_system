"""
Rate Calculation System
"""

import argparse
import sys

from validators import validate_loan_amount
from market_importer import import_csv
from loan_calculator import calculate_loan


def _get_args():
    """
    Get user arguments

    :returns: the populated namespace provided by argparse.ArgumentParser.parse_args
    """
    parser = argparse.ArgumentParser(description='Rate Calculation System')
    parser.add_argument('market_file', type=str, help='Market CSV File')
    parser.add_argument('loan_amount', type=validate_loan_amount, help='Loan Amount')
    parser.add_argument('duration', nargs='?', type=int, default=36,
                        help='the duration of the loan (default: %(default)s)')

    args = parser.parse_args()

    return args


def _print_results(requested_amount, rate, monthly_repayment, \
                   total_repayment):
    """
    Prints final results

    :param requested_amount: the requested loan amount
    :param rate: the loan's rate
    :param monthy_repayment: the monthly repayment amount
    :param total_repayment: the total repayment amount
    """
    print("Requested amount: £{}".format(requested_amount))
    print("Rate: {0:.1f}%".format(rate*100))
    print("Monthly repayment: £{0:.2f}".format(monthly_repayment))
    print("Total repayment: £{0:.2f}".format(total_repayment))


def main():
    """
    Main function
    """
    args = _get_args()
    market_data = import_csv(args.market_file)

    rate, monthly_repayment, total_repayment = calculate_loan(market_data,\
                                                              args.loan_amount,\
                                                              args.duration)

    _print_results(args.loan_amount, rate, monthly_repayment, total_repayment)


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print("ERROR: {}".format(ex))
        sys.exit(1)
