class Variable:
    letter: str
    degree: int

    def __init__(self, lett: str, deg: int = 1) -> None:
        self.degree = deg
        self.letter = lett
class Monomial:
    degree: int = 0
    variables: list[Variable] = []
    coefficient: float = 1

    def combine_vars(self):
        to_ret: list[str] = []
        for item in self.variables:
            to_ret.append(item.letter + "^" + str(item.degree) if item.degree != 1 else item.letter)
        return "".join(to_ret)

    def as_string(self):
        return str(self.coefficient if self.coefficient != 1 else "") + self.combine_vars()
