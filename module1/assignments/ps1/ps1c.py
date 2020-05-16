""" Problem Set 1
Part C: Finding the right amount to save away

Write a program to calculate the best savings rate, as a function of your starting salary.
You should use bisection search to help you do this efficiently.
You should keep track of the number of steps it takes your bisections search to finish.
You should be able to reuse some of the code you wrote for part B in this problem.
"""
from typing import Tuple

# constants
SEMI_ANNUAL_RAISE = 0.07
ANNUAL_RETURN = 0.04
DOWN_PAYMENT_RATE = 0.25
TOTAL_COST = 1000000
PORTION_DOWN_PAYMENT = TOTAL_COST * DOWN_PAYMENT_RATE
MONTHS = 36
BUFFER = 100


def calculate_savings_rate(starting_salary: int) -> Tuple[float, float]:
    """Calculates the best savings rate and number of bisect steps required
    to calculate it, as a function of starting salary.

    Arguments:
        starting_salary {int} -- Starting salary

    Returns:
        Tuple[float, float] -- A tuple of rate and steps

    >>> calculate_savings_rate(150000)
    (0.4414, 12)
    >>> calculate_savings_rate(300000)
    (0.2226, 9)
    >>> calculate_savings_rate(10000)
    (0, 0)

    """


    rate_min = 0
    rate_max = 10000
    portion_saved = int((rate_max + rate_min) / 2)
    steps = 0
    possible_to_save = False

    while abs(rate_min - rate_max) > 1:
        steps += 1
        annual_salary = starting_salary
        monthly_savings = (annual_salary / 12) * (portion_saved / 10000)
        current_savings = 0.0

        # iterate over months and add up savings
        for current_month in range(1, MONTHS + 1):
            monthly_return = current_savings * (ANNUAL_RETURN / 12)
            current_savings = current_savings + monthly_return + monthly_savings

            # decide whether to update rate_min
            if abs(current_savings - PORTION_DOWN_PAYMENT) < BUFFER:
                rate_min = rate_max
                # save success
                possible_to_save = True
                break
            elif current_savings > PORTION_DOWN_PAYMENT + BUFFER:
                break

            # raise salary if it is time
            if current_month % 6 == 0:
                annual_salary += annual_salary * SEMI_ANNUAL_RAISE
                monthly_savings = (annual_salary / 12) * (portion_saved / 10000)

        # update low and high boundaries for rate
        if current_savings < PORTION_DOWN_PAYMENT - BUFFER:
            rate_min = portion_saved
        elif current_savings > PORTION_DOWN_PAYMENT + BUFFER:
            rate_max = portion_saved

        # calculate new portion_saved for next iteration
        portion_saved = int((rate_max + rate_min) / 2)

    # decide what to return
    if possible_to_save:
        return (portion_saved / 10000, steps)
    else:
        return (0, 0)


if __name__ == '__main__':
    # ask user for input
    salary = float(input("Your starting annual salary: "))
    # salary = 300000 #debug
    # calculate rate and steps
    (rate, steps) = calculate_savings_rate(salary)
    if rate == 0:
        print("It is not possible to pay the down payment in three years.")
    else:
        print(f"Best savings rate (%): {rate}")
        print(f"Steps in bisection search: {steps}")
