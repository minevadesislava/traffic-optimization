import simulated_annealing
from random import shuffle
from random import randrange
from copy import deepcopy


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other_city):
        delta_x = self.x - other_city.x
        delta_y = self.y - other_city.y
        return (delta_x ** 2 + delta_y ** 2) ** 0.5

    def __str__(self):
        return "{}, {}".format(self.x, self.y)


class Tour:
    def __init__(self, city_list):
        self.city_list = city_list

    def randomize(self):
        shuffle(self.city_list)

    def energy(self):
        distance = 0
        city_list = self.city_list
        for i in range(1, len(city_list)):
            distance += (city_list[i] - city_list[i - 1])

        return distance

    def __str__(self):
        result = ""
        for city in self.city_list:
            result +=  " | " + str(city)

        return result

class TourGenerator:
    def __init__(self, city_list):
        self.city_list = city_list
        self.num_cities = len(city_list)

    def generate_neighbour(self, current_tour):
        proposed_tour = Tour(deepcopy(current_tour.city_list))
        city_a = randrange(self.num_cities)
        city_b = randrange(self.num_cities)

        proposed_tour.city_list[city_a], \
        proposed_tour.city_list[city_b] = proposed_tour.city_list[city_b], proposed_tour.city_list[city_a]

        return proposed_tour

class TourEstimator:
    def energy(self, tour):
        return tour.energy()


if __name__ == "__main__":
    city_coords = [[60, 200],[180, 200],[80, 180],[140, 180],[20, 160],
                   [100, 160],[200, 160],[140, 140],[40, 120],[100, 120],
                   [180, 100],[60, 80],[120, 80],[180, 60],[20, 40],
                   [100, 40],[200, 40],[20, 20],[60, 20],[160, 20]]

    city_list = [City(coords[0], coords[1]) for coords in city_coords]
    start_tour = Tour(city_list)
    start_tour.randomize()
    print("Initial energy: {}".format(start_tour.energy()))

    optimizer = simulated_annealing.SimulatedAnnealing()
    estimator = TourEstimator()
    generator = TourGenerator(city_list)

    best_state, best_energy = optimizer.optimize(estimator, generator, initial_state=start_tour)

    print("Final energy: {}".format(best_energy))
