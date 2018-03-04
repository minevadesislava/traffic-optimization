from copy import deepcopy
from random import randrange
from town import *
import constants

def tweak_parameter(current, left_boundary, right_boundary, deviation):
	range_start = max(left_boundary, current - deviation)
	range_end = min(right_boundary, current + deviation)

	return randrange(range_start, range_end + 1)

def tweak_traffic_light(traffic_light):
	result = deepcopy(traffic_light)

	result.period = tweak_parameter(result.period, constants.MIN_PERIOD, constants.MAX_PERIOD, 4)

	result.ratio = tweak_parameter(result.ratio, constants.MIN_RATIO, constants.MAX_RATIO, 20)
	result.offset = tweak_parameter(result.offset, 0, result.period, result.period // 4)

	return result

class CityGenerator:
	def generate_neighbour(self, current_state):
		neighbour = deepcopy(current_state)
		
		num_lights = neighbour.traffic_lights_count()
		traffic_light_index = randrange(num_lights)

		traffic_light = neighbour.get_traffic_light(traffic_light_index)
		traffic_light = tweak_traffic_light(traffic_light)

		neighbour.set_traffic_light(traffic_light_index, traffic_light)

		return neighbour

	def generate_random(self):
		pass

class CityEstimator:
	def energy(self, starting_state, t_steps=1000):
		current_state = deepcopy(starting_state)		
		current_state.restart_minute_count()

		for t in range(t_steps):
			current_state = current_state.move()

		energy = current_state.total_minute_count()
		return energy

count = 0
for i in range(100000):
	traffic_light = TrafficLight(6, 33, 1)
	tweaked = tweak_traffic_light(traffic_light)
	if (tweaked.offset > 2):
		# print("Period: {}, Ratio: {}, Offset: {}".format(tweaked.period, tweaked.ratio, tweaked.offset))
		count += 1

print(count)


		