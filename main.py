from pycmath import *

# print([mon.as_string() for mon in Polynomial("2x^2+3").members])
# TODO calculate -+ sign, should be -.




sys = EquationSystem(Equation("1x - 1y = 0"), Equation("1x + 1y = 2"))
print(solve_system_of_equations(sys))
# print([mon.as_string() for mon in eq.members])
# print([mon.as_string() for mon in eq.member1.members], "other is", [mon.as_string() for mon in eq.member2.members])
