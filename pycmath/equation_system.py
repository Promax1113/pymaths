from .equation import Equation, Result


class Result_EqSys(Result):
    x3: float
    x4: float

    def __init__(self, x_1, x_2, x_3, x_4):
        self.x1 = x_1
        self.x2 = x_2
        self.x3 = x_3
        self.x4 = x_4

    def values(self):
        return {"x1": self.x1, "x2": self.x2, "x3": self.x3, "x4": self.x4, "from_operation": self.from_operation}


class EquationSystem:
    equation_1: Equation
    equation_2: Equation

    def __init__(self, eq_1: Equation, eq_2: Equation):
        self.equation_1 = eq_1
        self.equation_2 = eq_2

def solve_system(sys: EquationSystem):
    print("{",[ mon.as_string() for mon in sys.equation_1.member1.members], "=", [mon.as_string() for mon in sys.equation_1.member2.members])
    print("{",[mon.as_string() for mon in sys.equation_2.member1.members] , "=", [mon.as_string() for mon in sys.equation_2.member2.members])
