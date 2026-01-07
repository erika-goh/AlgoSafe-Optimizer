import numpy as np
import random

SWARM_SIZE = 10
ITERATIONS = 30
C1, C2 = 1.5, 1.5
W = 0.5
NODES = 5  #number of nodes in the simulated network

class Particle:
    def __init__(self):
        #fixed start (0) and end (NODES-1), random middle nodes
        middle = list(range(1, NODES-1))
        random.shuffle(middle)
        self.position = [0] + middle + [NODES-1]
        self.velocity = [random.uniform(-1, 1) for _ in range(len(self.position))]
        self.best_position = self.position[:]
        self.best_fitness = float('inf')

def route_fitness(route, risks):
    return sum(risks[node] for node in route)

def optimize_route(seed=None):
    if seed is not None:
        np.random.seed(seed)  #seed NumPy
        random.seed(seed)     #seed Python's random

    risks = np.random.uniform(0, 1, NODES)  #simulated risk per node
    
    swarm = [Particle() for _ in range(SWARM_SIZE)]
    global_best_position = min(swarm, key=lambda p: route_fitness(p.position, risks)).position
    global_best_fitness = route_fitness(global_best_position, risks)
    
    for _ in range(ITERATIONS):
        for particle in swarm:
            fitness = route_fitness(particle.position, risks)
            
            if fitness < particle.best_fitness:
                particle.best_fitness = fitness
                particle.best_position = particle.position[:]
            
            if fitness < global_best_fitness:
                global_best_fitness = fitness
                global_best_position = particle.position[:]
            
            for i in range(len(particle.velocity)):
                particle.velocity[i] = (W * particle.velocity[i] +
                                        C1 * random.random() * (particle.best_position[i] - particle.position[i]) +
                                        C2 * random.random() * (global_best_position[i] - particle.position[i]))
                particle.position[i] = int(particle.position[i] + particle.velocity[i]) % NODES
    
    return global_best_position, global_best_fitness, risks
