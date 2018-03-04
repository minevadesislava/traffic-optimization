from random import randrange
import constants
class TrafficLight:
	def __init__(self, period=None, ratio=None, offset=None, capacity=10):
		self.period = period if period else randrange(constants.MIN_PERIOD, constants.MAX_PERIOD + 1)
		self.ratio = ratio if ratio else randrange(constants.MIN_RATIO, constants.MAX_RATIO + 1)
		self.offset = offset if offset else randrange(0, self.period + 1)
		self.counters = [0 for _ in range(4)]

	""" returns True iff at time this traffic light shows green on its LEFT - RIGHT axis """
	def traffic_color(self, time):
		reduced = (self.offset + time) % self.period
		green_time = round(self.period * ((self.ratio) / 100))
		return reduced < green_time

	def __str__(self):
		return "Traffic Light: Period={}, Ratio={}, Offset={}, Counters={}".format(self.period, self.ratio, self.offset, self.counters)
		

	def clear_counters(self):
		self.counters = [0 for _ in range(4)]




class City:
	pass


class TrafficCheckpoint:
	pass



# light = TrafficLight()
# light.counters = [i ** 2 for i in range(4)]
# # print(light)
# print (light)
# light.clear_counters()
# print (light)

# for i in range(28):
# 	print("Color == Green == {} for i == {}".format(light.traffic_color(i), i))
