"""
Rate Calculation System
"""

import argparse
import sys

from validators import validate_loan_amount
from market_importer import import_csv
from loan_calculator import calculate_loan


def _get_args(cli_params):
    """
    Get user arguments

    :returns: the populated namespace provided by argparse.ArgumentParser.parse_args
    """
    parser = argparse.ArgumentParser(description='Rate Calculation System')
    parser.add_argument('market_file', type=str, help='Market CSV File')
    parser.add_argument('loan_amount', type=validate_loan_amount, help='Loan Amount')
    parser.add_argument('duration', nargs='?', type=int, default=36,
                        help='the duration of the loan (default: %(default)s)')

    args = parser.parse_args(cli_params)

    return args


def _format_report(requested_amount, rate, monthly_repayment,
                   total_repayment):
    """
    Format final report

    :param requested_amount: the requested loan amount
    :param rate: the loan's rate
    :param monthly_repayment: the monthly repayment amount
    :param total_repayment: the total repayment amount
    :returns: a list with the text of the report
    """
    report = list()
    report.append("Requested amount: GBP {}".format(requested_amount))
    report.append("Rate: {0:.1f}%".format(rate*100))
    report.append("Monthly repayment: GBP {0:.2f}".format(monthly_repayment))
    report.append("Total repayment: GBP {0:.2f}".format(total_repayment))
    return report


def _print_results(requested_amount, rate, monthly_repayment,
                   total_repayment):
    """
    Prints final results

    :param requested_amount: the requested loan amount
    :param rate: the loan's rate
    :param monthly_repayment: the monthly repayment amount
    :param total_repayment: the total repayment amount
    """
    [print(x) for x in _format_report(requested_amount, rate,
                                      monthly_repayment, total_repayment)]


def main():
    """
    Main function
    """
    args = _get_args(sys.argv[1:])
    market_data = import_csv(args.market_file)

    rate, monthly_repayment, total_repayment = calculate_loan(market_data,
                                                              args.loan_amount,
                                                              args.duration)

    _print_results(args.loan_amount, rate, monthly_repayment, total_repayment)


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print("ERROR: {}".format(ex))
        sys.exit(1)
