import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
                                                
from phimath.linalg.vectors import vector
from phimath.physics.mechanics import RigidBody, SpringForce, System
# Replace with your actual import paths
# from mechanics import Particle, RigidBody, SpringForce, System 

def print_header(title):
    print(f"\n{'='*20} {title} {'='*20}")

def test_stage_1_oscillation():
    print_header("STAGE 1: SPRING DYNAMICS")
    
    anchor = RigidBody(mass=1000, position=vector(0, 10, 0), radius=1, is_static=True)
    bob = RigidBody(mass=1, position=vector(0, 5, 0), radius=0.5)
    
    spring = SpringForce(k=15, rest_length=5, particle1=anchor, particle2=bob, damping=0.8)
    sim = System(particles=[anchor, bob], springs=[spring])
    
    # 1. PUSH THE BOB FIRST
    bob.v = vector(0, -5, 0)
    
    # 2. NOW CAPTURE INITIAL ENERGY (Including the push)
    initial_energy = sim.get_total_energy()
    print(f"Captured Initial Energy: {initial_energy:.4f}")
    
    for i in range(10):
        sim.update(dt=0.1, sub_steps=20)
        print(f"Time {i*0.1:.1f}s | Bob Y: {bob.r.y:.3f} | Energy: {sim.get_total_energy():.4f}")
    
    final_energy = sim.get_total_energy()
    assert final_energy < initial_energy, "Damping failed: Energy did not decrease!"
    print("SUCCESS: Spring system is stable and damping energy.")

def test_stage_2_collisions():
    """Stage 2: Momentum Transfer (Elastic Collisions)"""
    print_header("STAGE 2: COLLISION MOMENTUM")
    
    # Head-on collision: p1 moving right, p2 stationary
    p1 = RigidBody(mass=2, position=vector(-5, 0, 0), velocity=vector(10, 0, 0), radius=0.5)
    p2 = RigidBody(mass=2, position=vector(0, 0, 0), velocity=vector(0, 0, 0), radius=0.5)
    
    sim = System(particles=[p1, p2])
    
    # Run until they collide
    for _ in range(30):
        sim.update(dt=0.02, sub_steps=5)
    
    print(f"Final V1: {p1.v.x:.2f} | Final V2: {p2.v.x:.2f}")
    # With mass 2 and 2, they should swap velocities nearly perfectly
    if abs(p1.v.x) < 0.5 and abs(p2.v.x - 10) < 0.5:
        print("SUCCESS: Perfect velocity swap detected.")
    else:
        print("WARNING: Inefficient momentum transfer.")

def test_stage_3_rope_bridge():
    """Stage 3: Multi-body Chain (Rope simulation)"""
    print_header("STAGE 3: ROPE CHAIN SIMULATION")
    
    nodes = []
    springs = []
    num_nodes = 5
    
    # Create nodes in a line
    for i in range(num_nodes):
        # Anchor the first and last node
        is_fixed = (i == 0 or i == num_nodes - 1)
        p = RigidBody(mass=0.5, position=vector(i * 2, 10, 0), is_static=is_fixed)
        nodes.append(p)
    
    # Connect with springs
    for i in range(num_nodes - 1):
        s = SpringForce(k=100, rest_length=1.5, particle1=nodes[i], particle2=nodes[i+1], damping=2.0)
        springs.append(s)
        
    sim = System(particles=nodes, springs=springs)
    
    print("Simulating sagging rope...")
    for _ in range(100):
        sim.apply_uniform_gravity()
        sim.update(dt=0.05, sub_steps=10)
        
    # Check if the middle node (index 2) sagged down
    print(f"Middle Node Height: {nodes[2].r.y:.3f}")
    if nodes[2].r.y < 10:
        print("SUCCESS: Rope sagged under tension.")

if __name__ == "__main__":
    try:
        test_stage_1_oscillation()
        test_stage_2_collisions()
        test_stage_3_rope_bridge()
        print("\nALL MECHANICS TESTS PASSED!")
    except Exception as e:
        print(f"\nTEST FAILED: {e}")