"""
Loan Calculator
"""

import numpy as np


def _calculate_monthly_repayment(amount, rate, duration):
    """
    Calculates the monthly repayment

    :param amount: loan amount
    :param rate: monthly compounding interest
    :param duration: duration of the loan in months
    :returns: monthly repayment
    """
    m_rate = np.power(1.0 + rate, 1 / 12.0) - 1.0
    monthly_repayment = (m_rate * amount) / \
                        (1.0 - np.power(1.0 + m_rate, -duration))
    return monthly_repayment


def _calculate_total_repayment(monthly_repayment, duration):
    """
    Calculates the total repayment

    :param monthly_repayment: the monthly repayment
    :param duration: duration of the loan in months
    :returns: total repayment
    """
    return monthly_repayment * duration


def _calculate_contribution_rate(row, requested_amount):
    """
    Calculates the contribution rate for a lender
    depending on the contributed amount

    :param row: numpy.array that contains lender's rate and contributed amount
    :param requested_amount: loan amount
    :returns: the contribution rate
    """
    rate = row[0] * (row[1] / np.int64(requested_amount))
    return rate


def calculate_loan(market_data, requested_amount, duration):
    """
    Calculates the rate, monthly and total repayment
    of the loan for the requested amount

    :param market_data: numpy.ndarray with the market data
    :param requested_amount: the requested amount
    :param duration: the duration of the loan in months
    :returns: a list with the rate, monthly and total repayment
    :raises Exception: In case the market does not have sufficient offers
    """
    rate = None
    monthly_repayment = None
    total_repayment = None

    # Check if total amount of market is sufficient for the requested amount
    if market_data[:, 2].sum() < requested_amount:
        raise Exception("The market does not have sufficient offers")

    # Sort by rate
    market_data = market_data[market_data[:, 1].argsort()]

    # Calculate the cumulative sum
    cum_sum = market_data[:, 2].cumsum()

    # Slicing the available market for the loan
    target_idx = cum_sum.searchsorted(requested_amount)
    used_market = market_data[:target_idx+1, 1:]

    # In case we need a fraction of the last lender's available amount
    used_market[-1][1] -= cum_sum[target_idx] - requested_amount

    # Calculate the rate for each lender based on the contributed amount
    contribution_rate = np.apply_along_axis(_calculate_contribution_rate, 1, \
                                            used_market, requested_amount)
    rate = contribution_rate.sum()

    monthly_repayment = _calculate_monthly_repayment(requested_amount, \
                                                     rate, duration)

    total_repayment = _calculate_total_repayment(monthly_repayment, \
                                                 duration)

    return (rate, monthly_repayment, total_repayment)
