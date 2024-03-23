from pycmath import Coefficients, solve_quadratic_equation
from pycmath import Polynomial, Equation


try:
    eq = Polynomial("-7x^2 + 2x + 24")
    print(f"Solution to equation is: {solve_quadratic_equation(eq.get_coefficients())}")

except Exception as e:
    print(f"err: {e}")

print([mon.as_string() for mon in eq.members])
#print([mon.as_string() for mon in eq.member1.members], "other is", [mon.as_string() for mon in eq.member2.members])