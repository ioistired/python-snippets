from math import factorial as fac
P = lambda n, r: fac(n) // fac(n - r)
C = lambda n, r: P(n, r) // fac(r)

