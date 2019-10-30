import random

l = random.sample(range(10000), 100)

def findMax(arr):
	new_list = max(arr)
	return new_list

print findMax(l)
