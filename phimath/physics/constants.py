from phimath.math.constants import TWO_PI
"""
Physical constants for the PhiMath physics layer.
Values are provided in SI units (kg, m, s, A, K, mol, cd).
"""

# --- Fundamental Constants ---
# Universal Gravitational Constant (m^3 kg^-1 s^-2)
G = 6.67430e-11 

# Speed of light in vacuum (m/s)
C = 299792458 

# Planck constant (J s)
PLANCK = 6.62607015e-34
# Reduced Planck constant (J s)
H_BAR = PLANCK / (TWO_PI) # Using PI value internally

# Boltzmann constant (J/K)
K_B = 1.380649e-23

# --- Electromagnetic Constants ---
# Elementary charge (C)
Q_E = 1.602176634e-19

# Vacuum permittivity (F/m)
EPSILON_0 = 8.8541878128e-12

# Vacuum permeability (T m/A)
MU_0 = 1.25663706212e-6

# --- Earth and Standard Physics ---
# Standard acceleration due to gravity (m/s^2)
G_EARTH = 9.80665

# Astronomical Unit (m)
AU = 149597870700

# --- Mass Constants ---
# Mass of an electron (kg)
M_E = 9.1093837e-31

# Mass of a proton (kg)
M_P = 1.6726219e-27

# Solar Mass (kg) - Essential for Black Hole sims
M_SOLAR = 1.98847e30