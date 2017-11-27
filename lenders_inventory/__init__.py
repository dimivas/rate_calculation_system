"""
Lenders Inventory
"""

import uuid

_LENDERS_MAPPING = {}

def map_lender_to_uuid(lender_name):
    """
    Map lender's name to UUID

    :param lender_name: lender's ID (name)
    :returns: uuid value of the lender
    """
    if lender_name not in _LENDERS_MAPPING:
        _LENDERS_MAPPING[lender_name] = uuid.uuid4()
    return _LENDERS_MAPPING[lender_name]


def map_uuid_to_lender(lender_uuid):
    """
    Map lender's UUID to name

    :param lender_uuid: uuid value of the lender
    :returns: lender's ID (name)
    :raises ValueError: raises an exception if the UUID has not been found
    """
    if lender_uuid not in list(_LENDERS_MAPPING.values()):
        raise ValueError("UUID not found")
    for name in _LENDERS_MAPPING:
        if _LENDERS_MAPPING[name] == lender_uuid:
            return name
