from pycmath import Coefficients, solve_quadratic_equation
from pycmath import Polynomial, Equation

print([mon.as_string() for mon in Polynomial("1x^2-11x + 28").members])
#print(solve_quadratic_equation(Polynomial("1x^2-11x + 28").get_coefficients(), show_results=True))

#print([mon.as_string() for mon in eq.members])
#print([mon.as_string() for mon in eq.member1.members], "other is", [mon.as_string() for mon in eq.member2.members])