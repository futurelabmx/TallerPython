# FutureLab
# Primer taller de Python

# Balanceo estequiométrico de ecuaciones químicas

from chempy import balance_stoichiometry

reacts, products = balance_stoichiometry({"H2O", "CO2"}, {"C6H12O6", "O2"})
print(dict(reacts))
print(dict(products))
