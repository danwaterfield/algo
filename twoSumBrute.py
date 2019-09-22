# naive twosum
# create every single pair of elements, then check to see whether tuple sum == target
# slowwwwwwwwww

a = [2,7,11,15]
target = 20
# on^2 / o(1) time/space complexity
def twoSumBrute(a, target):
	for i in range(len(a)-1):
		for j in range(i+1, len(a)):
			if a[i] + a[j] == target:
				print(a[i], a[j])
				return True 
	return False
print(twoSumBrute(a, target))