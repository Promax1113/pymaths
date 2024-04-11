
class RuffiniResult:
    coefficients: list[float]
    remainder: float
    
    def __init__(self, coeff: list[float], remd: float):
        self.coefficients = coeff
        self.remainder = remd 
    
    def as_dict(self):
        return {"coefficients": self.coefficients, "remainder": self.remainder} 

def ruffini(multip: float, coefficients: list[float]):
    results = [coefficients[0]]
    coefficients.pop(0)
    for index in range(len(coefficients)):
        results.append((results[index] * multip) + coefficients[index])
    remainder = results.pop(-1)
    return RuffiniResult(coefficients, remainder)


class Tests:
    @staticmethod
    def test1():
        assert ruffini(2, [-3, 0, 4, 0, -5, 1]).as_dict() == {"coefficients": [-3, -6, -8, -16, -37], "remainder": -73}

    @staticmethod
    def test2():
        assert ruffini(2, [2, 0, -3, 5, 1]).as_dict() == {"coefficients": [2, 4, 5, 15], "remainder": 31}
