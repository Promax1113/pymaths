from pycmath import Polynomial
from pycmath import Coefficients, solve_quadratic_equation

pol = Polynomial("+x^2 - 5x - 14")
print([mon.as_string() for mon in pol.members])
