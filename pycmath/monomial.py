class Monomial:
    degree: int = 0
    variables: list[str] = []
    coefficient: float = 0

    def as_string(self):
        _temp = str(self.coefficient) if self.coefficient < 0 else ("+" + str(self.coefficient))
        return _temp + "".join(self.variables)
    
