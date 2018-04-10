# FutureLab
# Primer taller python

# Escribiendo fórmulas químicas 
from chempy import Substance

ferricyanide = Substance.from_formula("Fe(CN)6-3")
ferricyanide.composition == {0: -3, 26: 1, 6: 6, 7: 6}
print(ferricyanide.unicode_name)

print("%.3f" %ferricyanide.mass)
