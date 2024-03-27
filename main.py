from pycmath import Coefficients, solve_quadratic_equation, solve_incomplete_equation
from pycmath import Polynomial, Equation
from pycmath import EquationSystem, Result_EqSys, solve_system

# print([mon.as_string() for mon in Polynomial("2x^2+3").members])
# TODO calculate -+ sign, should be -.
sys = EquationSystem(Equation("2x + 2y = 4"), Equation("2x - 2y = 0"))
solve_system(sys)
# print([mon.as_string() for mon in eq.members])
# print([mon.as_string() for mon in eq.member1.members], "other is", [mon.as_string() for mon in eq.member2.members])
