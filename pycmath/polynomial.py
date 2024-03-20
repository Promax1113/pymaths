from .monomial import Monomial, Variable
from string import ascii_lowercase

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
        self.members = []
        self.coefficients = []

        mon = Monomial()

        while index < len(p):
            index = last_searched + 1 if last_searched != 0 else index
            mon = Monomial() if mon.coefficient == 1 else mon
            if index + 1 >= len(p):
                break
            current = p[index]
            if current.isdigit():
                coefs = ''
                coefs = current
                numbers_index = index + 1
                while numbers_index < len(p):
                    current_char = p[numbers_index]

                    match current_char.isdigit():
                        case True:
                            coefs += current_char
                            last_searched = numbers_index
                            numbers_index += 1
                        case False:
                            break

                print("Coefficents for this monomial are", coefs)
                if index - 1 >= 0 and self.check_operator(p[index-1]) and self.check_operator_type(p[index-1]) is False:
                    mon.coefficient = -float(coefs)
                else:
                    mon.coefficient = float(coefs)
                
                if index + 1 == len(p) or p[index + 1] not in list(ascii_lowercase):
                    self.members.append(mon)
                    mon = Monomial()

            elif current in list(ascii_lowercase):
                pass

            else:
                print(f"Char: {current} was not a number or letter.")
                index += 1
                last_searched = 0

        while index > len(p) + 999:
            if last_searched != 0:
                index = last_searched
                if index == len(p) or p[index] in str(self.members[-1].coefficient):
                    break
            print("did:", mon.coefficient)
            if mon.coefficient == 0:
                mon = Monomial()
                mon.variables = []
            print(index, len(p) - 1)
            #print(p[index].isdigit(), p[index].isalpha(), p[index])
            if p[index].isdigit():
                coefs = p[index]
                print("Current coefs are", coefs, index-1)
                last_searched = 0
                _ind = index + 1
                while _ind < len(p):
                    if p[_ind].isdigit():
                        coefs = coefs + p[_ind]
                        last_searched = _ind
                        _ind += 1
                    else:
                        break
                    print("Current coefs are", coefs, type(coefs))
                if index-1 >= 0:

                    if self.check_operator(p[index-1]):

                        if not self.check_operator_type(p[index-1]):
                            mon.coefficient = -float(coefs)
                        else:
                            mon.coefficient = float(coefs)
                else:
                    mon.coefficient = float(coefs)

                print("Coefs currently:", mon.coefficient, "index is ", index, last_searched)

                if index + 1 == len(p):
                    self.members.append(mon)
            elif p[index] in list(ascii_lowercase):

                _ind = index
                #print(_ind, len(p))
                had_exponent: bool = False
                deg: list = []
                print("Now coef is", mon.coefficient)

                while _ind < len(p):
                    if p[_ind] in list(ascii_lowercase):
                        if _ind + 2 < len(p):
                            if p[_ind + 1] == "^":
                                __ind = _ind + 2
                                while __ind < len(p):
                                    if p[__ind].isdigit():
                                        deg.append(p[__ind])
                                        __ind += 1
                                    else:
                                        print(p[__ind - 1], __ind - 1)
                                        break
                                mon.variables.append(Variable(p[_ind], int("".join(deg))))
                                had_exponent = True
                        else:
                            print("No Exp found")
                            mon.variables.append(Variable(p[_ind]))

                        if had_exponent is False:
                            _ind += 1
                        else:
                            _ind += len(deg) + 2
                        last_searched = _ind
                    else:
                        break
                self.members.append(mon)
                mon = Monomial()
                mon.variables = []
                continue

            else:
                #print("It was different!")
                last_searched += 1
                index += 1
                continue
            index += 1
    def get_coefficients(self):
        self.coefficients = [mon.coefficient for mon in self.members]
        return Coefficients(self.coefficients)
