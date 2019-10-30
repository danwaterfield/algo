


# selection sort algo, two parts. First part finds the smallest element 

def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)): #for each element in the arr [obviously here not an arr, but a list]
		if arr[i] < smallest: #if the value of i in the array is < that held in smallest_index here arr[0]
			smallest = arr[i] # then update smallest with the new value
			smallest_index = i  # and the smallest index with that new value to serve as the new benchmark
	return smallest_index

def selectionSort(arr):
	new_arr = [] #placeholder list
	for i in range(len(arr)): # weird syntax for a 'for i in arr' but hey.
		smallest = findSmallest(arr) # calls findSmallest on the arr, then 
		new_arr.append(arr.pop(smallest))
	
	return new_arr


l = [1, 5, 3, 2, 8, 321342, 3, 3423, 6, 74, 2]

print selectionSort(l)