from pycmath import Polynomial
from pycmath import ruffini

p1 = Polynomial("10x + 10")

res = ruffini(1, p1.get_coefficients())
print(res)