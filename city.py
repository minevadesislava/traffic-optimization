#!/usr/bin/env python3

from town import TrafficLight
import numpy as np

class City:
    # TODO: input distibution
    # lights ids start from 0 for the streets
    def __init__(self, lights_count, streets, checkpoints=3, capacity=10, lights=None, dist=(2, 1)):
        self.lights = lights if lights else [TrafficLight() for _ in range(lights_count)]
        self.lights_count  = len(self.lights)
        self.dist = dist
        self.map = { index: [None for _ in range(4)] for index in range(lights_count)}
        for (f, to, direction) in streets:
            self.map[f][direction] = (to, [0 for _ in range(checkpoints)])

        self.boundary_lights = [(index, direction) for index in range(self.lights_count)
                                 for direction in range(4) if self.map[index][direction] == None]

    def add_cars(self):
        for index, direction in self.boundary_lights:
            self.lights[index].counters[direction] += max(0, round(np.random.normal(self.dist[0], self.dist[1])))

    def clear_city(self):
        for light in self.lights:
            light.clear_counters()


city = City(4, [(0, 1, 1), (0, 2, 2), (1, 3, 2)])
city.add_cars()
# for light in city.lights:
#     print(light)

print(sum([city.lights[index].counters[direction] for index, direction in city.boundary_lights]) / len(city.boundary_lights))
city.clear_city()
print(sum([city.lights[index].counters[direction] for index, direction in city.boundary_lights]) / len(city.boundary_lights))
# print(city.map)
# for light in city.lights:
#     print(light)

# for light in city.boundary_lights:
#     print(light)