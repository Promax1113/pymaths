from pycmath import Polynomial
from pycmath import Coefficients, solve_quadratic_equation

pol = Polynomial("+1x - 5x - 14")
pol.get_coefficients()
print(pol.coefficients)
