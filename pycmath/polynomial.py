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

    #TODO Should split by operator instead of manually, simplifies parsing

    def __init__(self, polynomial: str) -> None:
        p = list(polynomial.replace(" ", ""))
        index = 0
        last_searched = 0
        mon = Monomial()
        while index < len(p):
            if last_searched != 0:
                index = last_searched
            if mon.coefficient == 0:
                mon = Monomial()
                mon.variables = []
            #print(index, len(p) - 1)
            #print(p[index].isdigit(), p[index].isalpha(), p[index])
            if p[index].isdigit():
                coef = [p[index]]
                last_searched = 0
                _ind = index + 1
                while _ind < len(p):
                    if p[_ind].isdigit():
                        coef.append(p[_ind])
                        last_searched = _ind
                        _ind += 1
                    else:
                        break
                if index-1 >= 0:
                    coef = "".join(coef)
                    print(coef)
                    if self.check_operator(p[index-1]):

                        if not self.check_operator_type(p[index-1]):
                            mon.coefficient = -float(coef)
                        else:
                            mon.coefficient = float(coef)
                    print("Coefs currently:", mon.coefficient)
                    if index + 1 == len(p):
                        self.members.append(mon)
            elif p[index].isalpha():

                _ind = index
                print(_ind, len(p))
                while _ind < len(p):
                    if p[_ind].isalpha():
                        mon.variables.append(p[_ind])
                        last_searched = _ind + 1
                        _ind += 1
                    else:
                        break

                self.members.append(mon)
                mon = Monomial()
                mon.variables = []
                continue

            else:
                print("It was different!")
                last_searched += 1
                index += 1
                continue
            index += 1
    def get_coefficients(self):
        self.coefficients = [mon.coefficient for mon in self.members]
        return self.coefficients