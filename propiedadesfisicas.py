# FutureLab
# Primer taller de Python

# Propiedades físicas de compuestos para su uso en química analítica 
from chempy import Substance
from chempy.properties.water_density_tanaka_2001 import water_density as rho
from chempy.units import to_unitless, default_units as u

water = Substance.from_formula('H2O')

for T_C in (10, 15, 17):
    concentration_H2O = rho(T=(273.15 + T_C)*u.kelvin, units=u)/water.molar_mass(units=u)
    print('[H2O] = %.2f M (at %d °C)' % (to_unitless(concentration_H2O, u.molar), T_C))
