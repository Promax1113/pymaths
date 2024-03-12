from pycmath import Polynomial
from pycmath import Coefficients, solve_quadratic_equation

print(solve_quadratic_equation(Coefficients([22, -70, 4])).get_values())
