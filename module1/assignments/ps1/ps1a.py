""" Problem Set 1
Part A: House Hunting

Write a program to calculate how many months it will take you to save up enough money for a down
payment. You will want your main variables to be floats, so you should cast user inputs to floats.
"""
from typing import Tuple

# constants
PORTION_DOWN_PAYMENT = 0.25
R = 0.04


def calculate_months(annual_salary: float,
                     portion_saved: float,
                     total_cost: float) -> Tuple[int, float]:
    """Calculates months need to to save downpayment

    Arguments:
        annual_salary {float} -- Annual salary
        portion_saved {float} -- Portion of salary saved monthly
        total_cost {float} -- Total cost of a house

    Returns:
        Tuple[int, float] -- month and downpayment information

    >>> calculate_months(120000, 0.1, 1000000)
    (183, 250000.0)
    >>> calculate_months(80000, 0.15, 500000)
    (105, 125000.0)

    """

    # initial values
    current_savings = 0.0
    needed_months = 0

    # define basic rates
    monthly_salary = annual_salary / 12
    needed_down_payment = total_cost * PORTION_DOWN_PAYMENT

    # iterate over months and add up savings
    while current_savings <= needed_down_payment:
        current_savings += current_savings * R / 12
        current_savings += portion_saved * monthly_salary
        needed_months += 1

    return needed_months, needed_down_payment


if __name__ == '__main__':
    # ask user for input
    salary = float(input("Your starting annual salary: "))
    saved = float(input("Your portion of salary to be saved: "))
    cost = float(input("The cost of your dream home: "))

    (months, down_payment) = calculate_months(salary,
                                              saved,
                                              cost)
    print(f"You will need {months} months to save for {down_payment} downpayment")
