def ruffini(multip: float, coefficients: list[float]):
    results = [coefficients[0]]
    coefficients.pop(0)
    for index in range(len(coefficients)):
        results.append((results[index] * multip) + coefficients[index])
    reminder = results.pop(-1)
    return {"coefficients": results, "remainder": reminder}


class Tests:
    @staticmethod
    def test1():
        assert ruffini(2, [-3, 0, 4, 0, -5, 1]) == {"coefficients": [-3, -6, -8, -16, -37], "remainder": -73}

    @staticmethod
    def test2():
        assert ruffini(2, [2, 0, -3, 5, 1]) == {"coefficients": [2, 4, 5, 15], "remainder": 31}
