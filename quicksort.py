import random

def quickSort(arr): # recursive implementation
	if len(arr) < 2: # best case, yay!
		return arr
	else:
		pivot = arr[0] # recursive case, base element in arr...
		less = [i for i in arr[1:] if i <= pivot] # is the second element in the array less than or equal to the one before it?
		greater = [i for i in arr[1:] if i > pivot] # is the second element in the arr > the one preceding?
		return quickSort(less) + [pivot] + quickSort(greater)

l = random.sample(range(10000), 1000)

print quickSort(l)