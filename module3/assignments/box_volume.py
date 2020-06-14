""" Exercise: Simple constrained non-linear optimization problem with scipy.minimize.
Objective: What should the length, width and height of the box be to maximise
           its' volume given max surface constraint.
"""

import numpy as np
from scipy.optimize import minimize

# we want surface area of the box to be less than or equal to this
MAX_SURFACE = 10

# set initial guesses to minimim
LENGTH_GUESS = 1
WIDTH_GUESS = 1
HEIGHT_GUESS = 1


def calc_volume(x):
    """function to calculate the volume of the box
    """
    return x[0] * x[1] * x[2]


def calc_surface(x):
    """function to calculate the surface area of the box
    """
    return 2 * x[0] * x[1] + 2 * x[0] * x[2] + 2 * x[1] * x[2]


def objective(x):
    """ Objective function for optimization.
    We want to maximize the volume, so here we return negative volume and try to minimise it later
    """
    return -calc_volume(x)


def constraint(x):
    """ Constraints of the box.
    We want surface area of the box to be less than or equal to MAX_SURFACE
    """
    return MAX_SURFACE - calc_surface(x)


# define scipy constraint object
cons = ({'type': 'ineq', 'fun': constraint})

# load initial guess values into numpy array
x0 = np.array([LENGTH_GUESS, WIDTH_GUESS, HEIGHT_GUESS])

# find solution
solution = minimize(objective,
                    x0,
                    method='SLSQP',
                    constraints=cons,
                    options={'disp': True})

# minimize returns optimal solution
x_optimal = solution.x  # array([-1.66666707, -1.66666713, -1.66666716])

# minimize also returns optimal negative solution, so we invert it
optimal_volume = -solution.fun  # -2.151657414467269

# now calculate optimale surface area of this object
optimal_surface = calc_surface(x_optimal)

print(f"Length: {x_optimal[0]}")
print(f"Width: {x_optimal[1]}")
print(f"Height: {x_optimal[2]}")
print(f"Volume: {optimal_volume}")
print(f"Surface area: {optimal_surface}")

"""
Optimization terminated successfully.    (Exit mode 0)
            Current function value: -2.151657414467269
            Iterations: 4
            Function evaluations: 21
            Gradient evaluations: 4
Length: 1.2909944727867015
Width: 1.290994455352175
Height: 1.2909944180130968
Volume: 2.151657414467269
Surface area: 9.999999999713689
"""
