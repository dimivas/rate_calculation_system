"""
Validators
"""
from argparse import ArgumentTypeError
from configparser import ConfigParser

_APP_CONFIG = ConfigParser()
_APP_CONFIG.read('app_config/config.ini')


def validate_header(header, delimiter):
    """
    CSV Header validator

    :param header: the header of the file
    :param delimiter: the CSV's delimiter
    :raises Exception: in case the header is invalid
    """
    valid_csv_header = _APP_CONFIG['CSV']['ValidHeader'].split(',')
    if delimiter.join(header) != delimiter.join(valid_csv_header):

        err_msg = "Invalid header of CSV file. Expecting: '{}'"\
            .format(delimiter.join(valid_csv_header))

        raise ValueError(err_msg)


def validate_loan_amount(value):
    """
    Loan amount validator

    :param value: the loan amount
    :raises ArgumentTypeError: in case the amoun is invalid
    """
    min_amount = int(_APP_CONFIG['Amount']['Min'])
    max_amount = int(_APP_CONFIG['Amount']['Max'])
    amount_increment = int(_APP_CONFIG['Amount']['Increment'])

    err_msg = "The loan amount must be between {} and {} inclusive, with an increment of {}"
    err_msg = err_msg.format(min_amount, max_amount, amount_increment)

    try:
        ivalue = int(value)
    except ValueError:
        raise ArgumentTypeError(err_msg)

    if ivalue < min_amount or \
       ivalue > max_amount or \
       ivalue % amount_increment != 0:
        raise ArgumentTypeError(err_msg)
    return ivalue


def validate_lenders_amount(value):
    """
    Lender's available amount validator

    :param value: the available amount
    :raises ValueError: in case the amount is not a positive integer value
    """
    if value <= 0:
        err_msg = "The lender's amount ({}) must be a positive integer"\
                .format(value)
        raise ValueError(err_msg)
    return value
