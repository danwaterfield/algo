class solution:
	def twoSum(self, nums, target):
		lookFor = {}
		for number, index in enumerate(nums):
			try:
				return lookFor[index], number
			except KeyError:
				lookFor.setdefault(target - index, number)

test_case = solution()
array = [1, 5, 7]

print(test_case.twoSum(array, 6))