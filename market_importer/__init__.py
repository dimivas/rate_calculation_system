"""
Market Importer
"""

import csv
import numpy as np

from validators import validate_header, validate_lenders_amount
from lenders_inventory import map_lender_to_uuid, map_uuid_to_lender


def _parse_row(lender, rate, available):
    """
    Parse row of Lenders CSV file

    :param lender: lender's ID (name)
    :param rate: lender's requested rate
    :param available: lender's available amount
    :returns: list of UUID of the lender, rate and available amount
    """
    norm_res = (map_lender_to_uuid(lender), float(rate), \
                validate_lenders_amount(int(available)))

    return norm_res


def import_csv(filename):
    """
    Import market CSV file

    :param filename: The path of the CSV file
    :returns: numpy.array of the data found in the CSV file
    :raises FileNotFoundError: in case the file is missing
    :raises PermissionError: insufficient file permissions
    """
    data_list = []

    with open(filename, newline='') as csvfile:
        # Find dialect of the given CSV file
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)

        headers = next(reader, None)
        validate_header(headers, dialect.delimiter)

        data_list = [_parse_row(*row) for row in reader]

    return np.array(data_list)
