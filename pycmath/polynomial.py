from .monomial import Monomial, Variable
from string import ascii_lowercase

class FormatError(Exception):
    pass



class Coefficients:
    a: float
    b: float
    c: float

    def __init__(self, coefs: list[float]):
        if len(coefs) > 3:
            print(coefs)
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
        operators = ["-", "+", "*", "/", "^"]

        p = list(polynomial.replace(" ", ""))
        if "=" in p:
            raise FormatError("Found unexpected equal sign!")
        index = 0
        last_searched = 0
        self.members = []
        self.coefficients = []

        mon = Monomial()

        while index < len(p):
            index = last_searched + 1 if last_searched != 0 and p[index-1] not in list(ascii_lowercase) else index
            mon = Monomial() if mon.coefficient == 1 else mon
            mon.variables = [] if mon.coefficient == 1 else mon.variables
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
                            index = last_searched if last_searched != 0 else index + 1
                            break

                print("Coefficents for this monomial are", coefs)
                if index - 1 >= 0 and self.check_operator(p[index-1]) and self.check_operator_type(p[index-1]) is False:
                    mon.coefficient = -float(coefs)
                else:
                    mon.coefficient = float(coefs)
                
                if index + 1 == len(p) or p[index + 1] not in operators + list(ascii_lowercase):
                    self.members.append(mon)
                    mon = Monomial()
                    mon.variables = []

            elif current in list(ascii_lowercase):
                local_ind = index
                degree: str = ""
                
                while local_ind < len(p):
                    match (p[local_ind] in list(ascii_lowercase)):
                        case True:
                            if local_ind + 2 < len(p) and p[local_ind+1] == "^":
                                loop_ind = local_ind + 2
                                
                                while loop_ind < len(p):
                                    match p[loop_ind].isdigit():
                                        case True:
                                            degree += p[loop_ind]
                                            loop_ind += 1
                                        case False:
                                            break
                            
                            mon.variables.append(Variable(p[local_ind], int(degree))) if degree != "" else mon.variables.append(Variable(p[local_ind]))
                            print(f"Appended {p[local_ind]}")
                            local_ind = local_ind + len(degree) + 2 if mon.variables[-1].degree != 1 else local_ind + 1
                        case False:
                            index = local_ind
                            break
                    self.members.append(mon)
                    mon = Monomial()
                    mon.variables = []
                    continue

            else:
                print(f"Char: {current} was not a number or letter.")
                index += 1
                last_searched = 0

        
    def get_coefficients(self):
        self.coefficients = [mon.coefficient for mon in self.members]
        return Coefficients(self.coefficients) if len(self.coefficients) <= 3 else self.coefficients
