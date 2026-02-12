from phimath.linalg.vectors import vector
from phimath.math import *
from phimath.physics.constants import G

class Particle:
    def __init__(self, mass, position=None, velocity=None):
        """
        Represents a physical point mass.
        mass: mass in kg
        position: vector(x, y, z)
        velocity: vector(vx, vy, vz)
        """
        self.mass = mass
        self.r = position if position else vector(0, 0, 0)
        self.v = velocity if velocity else vector(0, 0, 0)
        self.a = vector(0, 0, 0)

    def __repr__(self):
        return f"Particle(m={self.mass}, r={self.r}, v={self.v})"

def projectile_motion(v0, angle_deg, h0=0, g=9.81):
    """
    Calculates key metrics for a 2D projectile.
    v0: initial velocity magnitude
    angle_deg: launch angle in degrees
    """    
    theta = angle_deg * DEG_TO_RAD
    vx = v0 * cos(theta)
    vy = v0 * sin(theta)
    
    # Time of flight (to reach h=0)
    # 0 = h0 + vy*t - 0.5*g*t^2 -> quadratic formula
    from phimath.linalg.solvers import quadratic_solver
    _, t_flight = quadratic_solver(-0.5 * g, vy, h0)
    
    range_x = vx * t_flight
    max_height = h0 + (vy**2) / (2 * g)
    
    return {
        "time_of_flight": t_flight,
        "range": range_x,
        "max_height": max_height
    }

def net_force(*forces):
    """Calculates the resultant vector of multiple force vectors."""
    res = vector(0, 0, 0)
    for f in forces:
        res = res + f
    return res

def friction_force(normal_force_vec, mu, velocity_vec, static=False):
    """
    Calculates friction force vector.
    normal_force_vec: Normal force vector (points away from surface)
    mu: Coefficient of friction (static or kinetic)
    velocity_vec: Velocity of the object
    """
    f_mag = normal_force_vec.magnitude() * mu
    
    if velocity_vec.magnitude() == 0:
        # Static friction acts to oppose potential motion
        return f_mag # Magnitude only if direction is not specified
        
    # Kinetic friction acts opposite to velocity
    return velocity_vec.normalize() * (-f_mag)

def tension_1d(m1, m2, F_applied):
    """Standard calculation for tension between two masses on a string."""
    a = F_applied / (m1 + m2)
    T = m1 * a # Tension pulling m1
    return a, T

def law_of_gravitation(m1, m2, r_vec):
    """
    Newton's Law of Universal Gravitation.
    r_vec: Vector from m1 to m2.
    """
    dist = r_vec.magnitude()
    if dist == 0:
        raise ValueError("Distance cannot be zero.")
    
    force_mag = (G * m1 * m2) / (dist**2)
    # Force on m1 by m2 points toward m2 (along r_vec)
    return r_vec.normalize() * force_mag

def orbital_velocity(M_central, r):
    """Calculates circular orbital velocity."""
    return sqrt(G * M_central / r)

def escape_velocity(M_central, r):
    """Calculates velocity needed to escape a central mass."""
    return sqrt(2 * G * M_central / r)

def momentum(mass, velocity_vec):
    return velocity_vec * mass

def kinetic_energy(mass, velocity_vec):
    return 0.5 * mass * (velocity_vec.magnitude()**2)

def elastic_collision_1d(m1, m2, v1, v2):
    """
    Calculates final velocities for a 1D elastic collision.
    Derived from conservation of momentum and KE.
    """
    v1_f = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    v2_f = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    return v1_f, v2_f

def work_done(force_vec, displacement_vec):
    """W = F . d"""
    return force_vec.dot(displacement_vec)

def power(force_vec, velocity_vec):
    """P = F . v"""
    return force_vec.dot(velocity_vec)

def torque(force_vec, lever_arm_vec):
    """Torque = r x F"""
    return lever_arm_vec.cross(force_vec)

def potential_energy(mass, height, g=9.81):
    """PE = mgh"""
    return mass * g * height

def force(mass, acceleration_vec):
    """F = ma"""
    return acceleration_vec * mass 

def angular_momentum(mass, velocity_vec, position_vec):
    """L = r x (mv)"""
    return position_vec.cross(velocity_vec * mass)

def spring_force(k, displacement_vec):
    """Hooke's Law: F = -kx"""
    return displacement_vec * (-k)