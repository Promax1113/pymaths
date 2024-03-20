from pycmath import Coefficients, solve_quadratic_equation
from pycmath import Polynomial


eq = Polynomial("-20x + 200")
print([mon.as_string() for mon in eq.members])
#print([mon.as_string() for mon in eq.member1.members], "other is", [mon.as_string() for mon in eq.member2.members])