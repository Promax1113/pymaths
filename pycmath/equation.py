from math import sqrt, pow

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



class Coefficients:
    a: float
    b: float
    c: float

    def __init__(self, coefs: list[float]):
        if len(coefs) > 3:
            print("Could not complete!")
            raise ValueError("There are too many coefficients!")
        self.a = coefs[0]
        self.b = coefs[1]
        self.c = coefs[2]

    def get_coefs(self) -> dict:
        return {'a': self.a, 'b': self.b, 'c': self.c}



def solve_quadratic_equation(coef: Coefficients) -> Result:
    disc = pow(coef.b, 2) - (4 * coef.a * coef.c)
    if disc < 0:
        raise ValueError("There is no real solution!")
    
    pos = (-coef.b + sqrt(disc))/ (coef.a * 2)
    neg = (-coef.b - sqrt(disc))/ (coef.a * 2)
    return Result(neg, pos, "from_complete_quadratic")
    
class Tests:
    complete_quad: str = "from_complete_quadratic"
    @staticmethod
    def test1():
        assert solve_quadratic_equation(Coefficients([1, -5, -14])).get_values() == Result(-2.0, 7.0, Tests.complete_quad).get_values()
    # Should add more tests.
    @staticmethod
    def test2():
        assert solve_quadratic_equation(Coefficients([-1, 11, -28])).get_values() == Result(4.0, 7.0, Tests.complete_quad).get_values()

    @staticmethod
    def print_result(to_run):
        try:
            print(f"\nStarting test of {to_run.__name__}!")
            assert(to_run)
            print("Successful!\n")
        except:
            print(f"Failed {to_run.__name__}!")

if __name__ == "__main__":
    print("Starting tests!")
    
    Tests.print_result(Tests.test1)
    Tests.print_result(Tests.test2)