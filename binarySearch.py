def binarySearch(list, value): #2 inputs, the list of things to be searched, and the value you're looking for.
	low = 0
	high = len(list)-1 #last item in list, assumes this is a sorted list obviously!

	while low <= high: 
		mid = low + high
		guess = list[mid]
		if guess == value: #is the value the middle item in the list?  
			return mid
		if guess > value:
			high = mid-1 #if the midpoint value is higher than the actual value, then the new high becomes one less than the midpoint of the list
		else:
			low = mid +1 # on the other hand, if the midpoint is lower than the value then the new low becomes one value higher than the midpoint.
	return None

l = list(range(1,100000))


print binarySearch(l, 437)
