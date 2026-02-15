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
    RigidBody,
    Force,
    SpringForce,
    System,
    Newtonian,
    Lagrangian
)
from .vectorops import VectorOps, VectorField

__all__ = [
    'G', 'C', 'PLANCK', 'H_BAR', 'K_B', 'Q_E', 'EPSILON_0', 'MU_0', 'G_EARTH', 'AU', 'M_E', 'M_P', 'M_SOLAR',
    'Particle', 'RigidBody', 'Force', 'SpringForce', 'System', 'Newtonian', 'Lagrangian',
    'VectorOps', 'VectorField',
]