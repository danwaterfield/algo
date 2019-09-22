a = [2,7,11,15]
t = 9

def twoSum(a, target):
	ht = dict()
	for i in range(len(a)):
		if a[i] in ht:
			print(ht[a[i]], a[i])
			return True
		else:
			ht[target - a[i]] = a[i]

	return False


print(twoSum(a, t))

# o(n) time comp[lexity], ditto linear space complexity.