"""
Validators
"""
from argparse import ArgumentTypeError

_VALID_CSV_HEADER = ("Lender", "Rate", "Available")

_MIN_AMOUNT = 1000
_MAX_AMOUNT = 15000
_AMOUNT_INCREMENT = 100


def validate_header(header, delimiter):
    """
    CSV Header validator

    :param header: the header of the file
    :param delimiter: the CSV's delimiter
    :raises Exception: in case the header is invalid
    """
    if delimiter.join(header) != delimiter.join(_VALID_CSV_HEADER):

        err_msg = "Invalid header of CSV file. Expecting: '{}'"\
            .format(delimiter.join(_VALID_CSV_HEADER))

        raise ValueError(err_msg)


def validate_loan_amount(value):
    """
    Loan amount validator

    :param value: the loan amount
    :raises ArgumentTypeError: in case the amoun is invalid
    """
    err_msg = "The loan amount must be between {} and {} inclusive, with an increment of {}"
    err_msg = err_msg.format(_MIN_AMOUNT, _MAX_AMOUNT, _AMOUNT_INCREMENT)

    try:
        ivalue = int(value)
    except ValueError:
        raise ArgumentTypeError(err_msg)

    if ivalue < _MIN_AMOUNT or \
       ivalue > _MAX_AMOUNT or \
       ivalue % _AMOUNT_INCREMENT != 0:
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
