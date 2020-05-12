""" Problem Set 1
Part B: Saving with a raise

Write a program to calculate how many months it will take you save up enough money for a down payment. Assume that your investments earn a return of r = 0.04 (or 4%) and the required down payment percentage is 0.25 (or 25%).
"""
# constants
PORTION_DOWN_PAYMENT = 0.25
R = 0.04


def calculate_months(annual_salary: float,
                     portion_saved: float,
                     total_cost: float,
                     semi_annual_rase: float) -> int:
    """Calculates months need to to save downpayment with semi-annual raise in salary

    Arguments:
        annual_salary {float} -- Annual salary
        portion_saved {float} -- Portion of salary saved monthly
        total_cost {float} -- Total cost of a house
        semi_annual_rase {float} -- Semi annual raise in salary

    Returns:
        float -- Months needed for downpayment

    >>> calculate_months(120000, 0.05, 500000, 0.03)
    142
    >>> calculate_months(80000, 0.1, 800000, 0.03)
    159
    >>> calculate_months(75000, 0.05, 1500000, 0.05)
    261

    """

    # initial values
    current_savings = 0.0
    month_count = 0

    # define basic rates
    needed_down_payment = total_cost * PORTION_DOWN_PAYMENT

    # iterate over months and add up savings
    while current_savings <= needed_down_payment:
        if month_count != 0 and month_count % 6 == 0:
            annual_salary += annual_salary * semi_annual_rase

        current_savings += current_savings * R / 12
        current_savings += portion_saved * annual_salary / 12
        month_count += 1

    return month_count


if __name__ == '__main__':
    # ask user for input
    salary = float(input("Your starting annual salary: "))
    saved = float(input("Your portion of salary to be saved: "))
    cost = float(input("The cost of your dream home: "))
    salary_raise = float(input("Your semi annual raise in salary: "))

    months = calculate_months(salary,
                                saved,
                                cost,
                                salary_raise)
    print(f"You will need {months} months to save for downpayment")
