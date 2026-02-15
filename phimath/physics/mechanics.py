from phimath.calculas import differentiate
from phimath.linalg.vectors import vector
from .vectorops import VectorOps
from phimath.physics.constants import G, G_EARTH

class Particle:
    def __init__(self, mass, position=None, velocity=None, radius=0.5):
        self.mass = mass
        self.r = position if position else vector(0, 0, 0)
        self.v = velocity if velocity else vector(0, 0, 0)
        self.a = vector(0, 0, 0)
        self.radius = radius

    def kinetic_energy(self):
        return 0.5 * self.mass * self.v.magnitude()**2
    
    def potential_energy(self, other):
        r_vec = other.r - self.r
        r_mag = r_vec.magnitude()
        return -G * self.mass * other.mass / r_mag if r_mag > 0.01 else 0

    def __repr__(self):
        return f"Particle(m={self.mass}, r={self.r}, v={self.v})"

class RigidBody(Particle):
    def __init__(self, mass, position=None, velocity=None, radius=0.5, elasticity=1.0, is_static=False):
        super().__init__(mass, position, velocity, radius)
        self.elasticity = elasticity
        self.is_static = is_static

    def apply_force(self, force_obj):
        if self.is_static:
            return
        # Works with Force or SpringForce
        if hasattr(force_obj, 'to_vector'):
            self.a += force_obj.to_vector() / self.mass

    def collide(self, other):
        relative_pos = self.r - other.r
        distance = relative_pos.magnitude()
        min_dist = self.radius + other.radius

        if 0 < distance < min_dist:
            # Velocity update
            v1_final = (self.v * (self.mass - other.mass) + 2 * other.mass * other.v) / (self.mass + other.mass)
            v2_final = (other.v * (other.mass - self.mass) + 2 * self.mass * self.v) / (self.mass + other.mass)
            
            combined_e = (self.elasticity + getattr(other, 'elasticity', 1.0)) / 2
            self.v = v1_final * combined_e
            other.v = v2_final * combined_e

            # Position Correction
            overlap = min_dist - distance
            correction = relative_pos.normalize() * (overlap / 2)
            self.r += correction
            other.r -= correction

class Force:
    def __init__(self, magnitude, direction):
        self.magnitude = magnitude
        self.direction = direction.normalize()

    def to_vector(self):
        return self.magnitude * self.direction

class SpringForce:
    def __init__(self, k, rest_length, particle1, particle2, damping=0.0):
        """
        k: spring constant
        rest_length: equilibrium length
        p1, p2: connected particles
        damping: coefficient of friction (default 0)
        """
        self.k = k
        self.rest_length = rest_length
        self.p1 = particle1
        self.p2 = particle2
        self.damping = damping

    def apply(self):
        """Calculates tension and damping, then applies it."""
        r_vec = self.p2.r - self.p1.r
        r_mag = r_vec.magnitude()
        
        if r_mag > 0:
            # 1. Spring Force (Hooke's Law)
            unit_vector = r_vec.normalize()
            extension = r_mag - self.rest_length
            spring_f_mag = self.k * extension
            
            # 2. Damping Force
            # We only damp the velocity along the spring's axis
            relative_v = self.p2.v - self.p1.v
            # Dot product gives the scalar projection of velocity onto the spring vector
            v_along_spring = relative_v.dot(unit_vector) 
            damping_f_mag = self.damping * v_along_spring
            
            # Total Force Vector
            total_f_vec = unit_vector * (spring_f_mag + damping_f_mag)
            
            # Apply to particles (Equal and Opposite)
            self.p1.a += total_f_vec / self.p1.mass
            self.p2.a -= total_f_vec / self.p2.mass
    
    def e_potential_energy(self):
        r_mag = (self.p2.r - self.p1.r).magnitude()
        return 0.5 * self.k * ((r_mag - self.rest_length)**2)

    def __repr__(self):
        return f"SpringForce(k={self.k}, L0={self.rest_length}, c={self.damping})"
    
class System:
    def __init__(self, particles, springs=None):
        self.particles = particles
        self.springs = springs if springs else []

    def compute_gravitational_forces(self):
        for i in range(len(self.particles)):
            for j in range(i + 1, len(self.particles)):
                p1, p2 = self.particles[i], self.particles[j]
                r_vec = p2.r - p1.r
                r_mag = r_vec.magnitude()
                if r_mag > 0.1: # Softening to prevent explosions
                    f_mag = G * p1.mass * p2.mass / r_mag**2
                    f_vec = r_vec.normalize() * f_mag
                    if not getattr(p1, 'is_static', False): p1.a += f_vec / p1.mass
                    if not getattr(p2, 'is_static', False): p2.a -= f_vec / p2.mass

    def resolve_collisions(self):
        for i in range(len(self.particles)):
            for j in range(i + 1, len(self.particles)):
                if isinstance(self.particles[i], RigidBody) and isinstance(self.particles[j], RigidBody):
                    self.particles[i].collide(self.particles[j])

    def get_total_energy(self):
        ke = sum(p.kinetic_energy() for p in self.particles)
        # Summing GP and EP
        gp = 0
        for i in range(len(self.particles)):
            for j in range(i + 1, len(self.particles)):
                gp += self.particles[i].potential_energy(self.particles[j])
        ep = sum(s.e_potential_energy() for s in self.springs)
        return ke + gp + ep

    def apply_uniform_gravity(self, g_vector=vector(0, -G_EARTH, 0)):
        for p in self.particles:
            if not getattr(p, 'is_static', False):
                # F = m * g
                p.a += g_vector

    def update(self, dt, sub_steps=4, gravity=vector(0, -G_EARTH, 0)):
        sub_dt = dt / sub_steps
        for _ in range(sub_steps):
        # 1. Reset
            for p in self.particles: p.a = vector(0, 0, 0)
        
        # 2. Apply Global Gravity (Moved inside the loop)
            if gravity:
                self.apply_uniform_gravity(gravity)
            
        # 3. Apply Internal Forces
            self.compute_gravitational_forces()
            for s in self.springs: s.apply()
        
        # 4. Resolve and Integrate
            self.resolve_collisions()
            for p in self.particles:
                if not getattr(p, "is_static", False):
                    p.v += p.a * sub_dt
                    p.r += p.v * sub_dt

class Newtonian(System):
    def __init__(self, particles, springs=None):
        super().__init__(particles, springs)

    def solve(self,duration,  dt, sub_steps=1000, gravity=None):
        steps = int(duration / dt)
        for _ in range(steps):
            self.update(dt, sub_steps=sub_steps, gravity=gravity)

    def get_positions(self):
        return [p.r for p in self.particles]
    
from array import array
from phimath.calculas.differentiate import differentiate
from phimath.calculas.ode_solvers import rk4

class Lagrangian:
    """
    Analytical engine to solve Euler-Lagrange equations for system positions.
    """
    def __init__(self, system, potential_func):
        self.system = system
        self.potential_func = potential_func

    def _get_L(self, positions, velocities):
        """
        Computes L = T - V for arbitrary state vectors.
        Used for numerical differentiation.
        """
        # Kinetic Energy T = 1/2 m v^2
        ke = 0.0
        for i in range(self.system.n):
            v_sq = sum(velocities[i*3 + j]**2 for j in range(3))
            ke += 0.5 * self.system.mass[i] * v_sq
            
        # Potential Energy V from user-defined function
        # Temporarily update system state to use potential_func
        original_pos = self.system.pos
        self.system.pos = array('d', positions)
        pe = self.potential_func(self.system)
        self.system.pos = original_pos
        
        return ke - pe

    def solve_step(self, dt):
        """
        Solves the Euler-Lagrange equations to find accelerations 
        and updates the system's position.
        """
        n_params = self.system.n * 3
        accelerations = [0.0] * n_params
        
        # Numerical approximation of d/dt(dL/dv) - dL/dq = 0
        # For simple Cartesian systems, this reduces to finding 
        # the gradient of the potential field.
        h = 1e-5
        for i in range(n_params):
            # Partial L / Partial q
            def L_q(val):
                p = list(self.system.pos)
                p[i] = val
                return self._get_L(p, self.system.vel)
            
            dL_dq = differentiate(L_q, self.system.pos[i], h)
            
            # For most classical mechanics: accel = (dL/dq) / mass
            mass_idx = i // 3
            self.system.acc[i] = dL_dq / self.system.mass[mass_idx]

        # Integrate to update velocity and position
        for i in range(n_params):
            self.system.vel[i] += self.system.acc[i] * dt
            self.system.pos[i] += self.system.vel[i] * dt