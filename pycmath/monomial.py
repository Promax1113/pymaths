class Monomial:
    degree: int = 0
    variables: list[str] = []
    coefficient: float = 0

    def as_string(self):
        return str(self.coefficient) + "".join(self.variables)
