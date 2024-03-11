from pycmath import Polynomial
from pycmath import Monomial

p = Polynomial("-1x")
print("len is",len(p.members))
for mon in p.members:
    print(mon.as_string())
