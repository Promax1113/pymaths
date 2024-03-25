from pycmath import Coefficients, solve_quadratic_equation
from pycmath import Polynomial, Equation

# print([mon.as_string() for mon in Polynomial("2x^2+3").members])
# TODO calculate -+ sign, should be -.
print(solve_quadratic_equation(Equation("6x^2 + 11x - 35 = 0").member1.get_coefficients()).values())

# print([mon.as_string() for mon in eq.members])
# print([mon.as_string() for mon in eq.member1.members], "other is", [mon.as_string() for mon in eq.member2.members])
