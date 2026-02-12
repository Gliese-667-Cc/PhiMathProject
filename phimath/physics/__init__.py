"""
Physics layer for PhiMath.

This package provides high-level abstractions for classical mechanics, 
kinematics, and gravitation, built on top of the PhiMath symbolic 
and numerical engines.
"""

from .constants import (
    G, 
    C, 
    PLANCK, 
    H_BAR, 
    K_B, 
    Q_E, 
    EPSILON_0, 
    MU_0, 
    G_EARTH, 
    AU, 
    M_E, 
    M_P, 
    M_SOLAR
)

from .mechanics import (
    Particle,
    projectile_motion,
    net_force,
    friction_force,
    tension_1d,
    law_of_gravitation,
    orbital_velocity,
    escape_velocity,
    momentum,
    kinetic_energy,
    elastic_collision_1d,
    work_done,
    power,
    torque,
    potential_energy,
    force,
    angular_momentum,
    spring_force
)

__all__ = [
    # Fundamental Constants
    "G", "C", "PLANCK", "H_BAR", "K_B", 
    "Q_E", "EPSILON_0", "MU_0", "G_EARTH", 
    "AU", "M_E", "M_P", "M_SOLAR",

    # Kinematics & Dynamics
    "Particle",
    "projectile_motion",
    "net_force",
    "friction_force",
    "tension_1d",
    "force",
    "spring_force",

    # Gravitation & Orbits
    "law_of_gravitation",
    "orbital_velocity",
    "escape_velocity",

    # Conservation Laws & Energy
    "momentum",
    "angular_momentum",
    "kinetic_energy",
    "potential_energy",
    "elastic_collision_1d",
    "work_done",
    "power",
    "torque"
]