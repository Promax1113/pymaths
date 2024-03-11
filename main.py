from pycmath import Polynomial
from pycmath import Monomial

p = Polynomial("-2x -7v")
print("len is",len(p.members))
for mon in p.members:
    print(mon.as_string())
