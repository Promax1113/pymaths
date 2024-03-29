from math import sqrt, pow
from .polynomial import Coefficients, Polynomial, FormatError


class ResultError(Exception):
    pass


class Equation:
    member1: Polynomial
    member2: Polynomial

    def __init__(self, equation: str):
        equation = equation.replace(" ", "")
        if "=" not in list(equation):
            raise FormatError("Equal sign not found!")
        print(equation.split("=")[1])
        self.member1 = Polynomial(equation.split("=")[0])
        self.member2 = Polynomial(equation.split("=")[1])


class Result:
    x1: float
    x2: float
    from_operation = None

    def __init__(self, _x1, _x2, _from_operation=None):
        self.x1 = _x1
        self.x2 = _x2
        self.from_operation = _from_operation

    def values(self):
        return {
            'x1': self.x1,
            'x2': self.x2,
            'from_operation': self.from_operation if self.from_operation else "none specified"
        }


def solve_quadratic_equation(coef: Coefficients | Polynomial, show_results: bool = False):
    if type(coef) == type(Polynomial):
        coef = coef.get_coefficients()

    disc = pow(coef.b, 2) - (4 * coef.a * coef.c)
    if disc < 0:
        raise ResultError("There is no real solution!")

    pos = (-coef.b + sqrt(disc)) / (coef.a * 2)
    neg = (-coef.b - sqrt(disc)) / (coef.a * 2)
    result = Result(neg, pos, "from_complete_quadratic")
    return result if show_results is False else result.values()


def solve_incomplete_equation(polynomials: Equation, show_results: bool = False):
    # TODO should try to check if they are all on the same side!
    pol = (polynomials.member1 if len(polynomials.member1.members) > len(
        polynomials.member2.members) else polynomials.member2).get_coefficients()
    print(pol.values())
    # !! I don't know how I would check if it's been modified!
    if pol.a != 1 and pol.b != 1:
        return solve_incomplete_a_b(pol.a, pol.b)
    elif pol.a != 1 and pol.c != 1:
        return solve_incomplete_a_c(pol.a, pol.c)


# Works but super unreliably!
def solve_incomplete_a_b(a: float, b: float):
    # this means this one is x^2 + 2x, which also means I should extract common factor or x(x-2)
    return Result(0, (-(b / a)), "from_incomplete_ab")


# Working unreliably!
def solve_incomplete_a_c(a: float, c: float):
    # This means it is x^2 + 4 that transforms to x = sqrt(-4) and x1 = 2, x2 = -2
    c = -c / a
    if not c >= 0:
        raise ResultError(f"There is no real solution to sqrt({-c}).")
    res = sqrt(c)
    return Result(res, -res, "from_incomplete_ac")


class Tests:
    incompl_ab = "from_incomplete_ab"
    incompl_ac = "from_incomplete_ac"
    complete_quad: str = "from_complete_quadratic"

    @staticmethod
    def test1():
        assert solve_quadratic_equation(Polynomial("1x^2 - 5x - 14").get_coefficients(), show_results=True) == Result(
            # type: ignore
            -2.0, 7.0, Tests.complete_quad).values()

    # Should add more tests.
    @staticmethod
    def test2():
        assert solve_quadratic_equation(Polynomial("1x^2-11x + 28").get_coefficients(), show_results=True) == Result(
            # type: ignore
            4.0, 7.0, Tests.complete_quad).values()

    @staticmethod
    def test3():
        assert solve_incomplete_equation(Equation("3x^2+4x=0")).values() == Result(0, -1.3333333333333333, Tests.incompl_ab)
    
    @staticmethod
    def test4():
        assert solve_incomplete_equation(Equation("5x^2-20=0")).values() == Result(2, -2, Tests.incompl_ac)

    @staticmethod
    def print_result(to_run):
        #try:
        print(f"\nStarting test of {to_run.__name__}!")
        to_run()
        print("Successful!\n")
        #except Exception as e:
        #    print(f"Failed {to_run.__name__}! Err: {e.args}")


if __name__ == "__main__":
    print("Starting tests!")
    Tests.print_result(Tests.test1)
    Tests.print_result(Tests.test2)
    Tests.print_result(Tests.test3)
    Tests.print_result(Tests.test4)