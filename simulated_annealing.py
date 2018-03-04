import numpy as np
from random import random
class SimulatedAnnealing:
    def __init__(self, initial_temp = 10000, annealing_rate = 0.003):
        self.initial_temp = initial_temp
        self.annealing_rate = annealing_rate

    @staticmethod
    def acc_prob(current, neighbour, temperature):
        return min(1.0, np.exp((current - neighbour) / temperature))



    def optimize(self, estimator, generator, initial_state=None):
        current_state = initial_state if initial_state else generator.generate_random() 
        best_state = current_state
        current_energy = estimator.energy(current_state)
        best_energy = current_energy
        
        temperature = self.initial_temp
        while temperature > 1:
            neighbour_state = generator.generate_neighbour(current_state)
            neighbour_energy = estimator.energy(neighbour_state)

            if self.acc_prob(current_energy, neighbour_energy, temperature) > random():
                current_state = neighbour_state
                current_energy = neighbour_energy

            if current_energy < best_energy:
                best_state = current_state
                best_energy = current_energy


            temperature *= (1 - self.annealing_rate)

        return best_state, best_energy




