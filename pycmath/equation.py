from math import sqrt, pow
from .polynomial import Coefficients, Polynomial
class Equation:
    member1: Polynomial
    member2: Polynomial

    def __init__(self, equation: str):
        equation = equation.replace(" ", "")
        print(equation.split("=")[1])
        print([mon.as_string() for mon in Polynomial(equation.split("=")[0]).members], "mem1")
        print([mon.as_string() for mon in Polynomial(equation.split("=")[1]).members], "mem2")
        #self.member1 = Polynomial(equation.split("=")[0])
        #self.member2 = Polynomial(equation.split("=")[1])
class Result:
    x1: float
    x2: float
    from_operation = None
    def __init__(self, _x1, _x2, _from_operation = None):
        self.x1 = _x1
        self.x2 = _x2
        self.from_operation = _from_operation

    def get_values(self):
        return {
            'x1': self.x1,
            'x2': self.x2,
            'from_operation': self.from_operation if self.from_operation else "none specified"
        }






def solve_quadratic_equation(coef: Coefficients, show_results: bool = False):
    disc = pow(coef.b, 2) - (4 * coef.a * coef.c)
    if disc < 0:
        raise ValueError("There is no real solution!")

    pos = (-coef.b + sqrt(disc))/ (coef.a * 2)
    neg = (-coef.b - sqrt(disc))/ (coef.a * 2)
    result = Result(neg, pos, "from_complete_quadratic")
    return result if show_results is False else result.get_values()


def solve_incomplete_equation(polynomials: Equation, show_results: bool = False):
    member_deg_1 = [mon.degree for mon in polynomials.member1.members]
    member_deg_2 = [mon.degree for mon in polynomials.member2.members]


class Tests:
    complete_quad: str = "from_complete_quadratic"
    @staticmethod
    def test1():
        assert solve_quadratic_equation(Coefficients([1, -5, -14])).get_values() == Result(-2.0, 7.0, Tests.complete_quad).get_values()
    # Should add more tests.
    @staticmethod
    def test2():
        assert solve_quadratic_equation(Coefficients([1, -11, 28])).get_values() == Result(4.0, 7.0, Tests.complete_quad).get_values()

    @staticmethod
    def print_result(to_run):
        try:
            print(f"\nStarting test of {to_run.__name__}!")
            to_run()
            print("Successful!\n")
        except:
            print(f"Failed {to_run.__name__}!")

if __name__ == "__main__":
    print("Starting tests!")
    print(Result(-2.0, 7.0, Tests.complete_quad).get_values() == solve_quadratic_equation(Coefficients([1, -5, -14])).get_values() )

    Tests.print_result(Tests.test1)
    Tests.print_result(Tests.test2)
