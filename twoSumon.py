

def twoSum(a, target):
	i = 0
	j = len(a) - 1

	while i <= j:
		if a[i] + a[j] == target:
			print(a[i], a[j])
			return True
		elif a[i] + a[j] < target:
			i += 1
		else: 
			j -= 1
	return False


a = [2,7,11,15, 17, 19]
target = 9
print(twoSum(a, target))

#this is of course in o-n time, but the real issue is getting it to print the indices, 
# which would require enumerate, but also reworking the entire code...