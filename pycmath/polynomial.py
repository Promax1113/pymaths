from typing import _ProtocolMeta
from .monomial import Monomial

class Polynomial:
    members: list[Monomial] = []
    degree: int = 0
    coefficients: list[float] = []

    @staticmethod
    def check_vector_size(index: int, size: int):
        if index > size-1:
            return False
        else:
            return True

    @staticmethod
    def check_operator(char: str):
        return True if char == '-' or char == '+' else False

    @staticmethod
    def check_operator_type(char: str):
        return True if char == '+' else False

    def __init__(self, polynomial: str) -> None:
        p = list(polynomial.replace(" ", ""))
        index = 0
        last_searched = 0

        while index < len(p):
            if last_searched != 0:
                index = last_searched

            mon = Monomial()
            print(p[index].isdigit(), p[index])
            if p[index].isdigit():
                coef = [p[index]]
                last_searched = 0
                for c in p:
                    if c.isdigit():
                        coef.append(c)
                        last_searched = p.index(c)
                    else:
                        break
                if index-1 >= 0:
                    coef = "".join(coef)
                    if self.check_operator(p[index-1]):

                        if not self.check_operator_type(p[index-1]):
                            mon.coefficient = -float(coef)
                        else:
                            mon.coefficient = float(coef)
                    print("Coefs currently:", mon.coefficient)
            elif p[index].isalpha():
                for i in p:
                    if i.isalpha:
                        mon.variables.append(i)
                        last_searched = p.index(i)
                    else:
                        break
            else:
                print("It was different!")
                index += 1
                continue
            self.members.append(mon)
            index += 1
