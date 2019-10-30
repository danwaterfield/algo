
#recursive algo to find the sum of items in a list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 100]
def sumList(arr):
	if arr == []:
		return 0
	return arr[0] + sumList(arr[1:])

print sumList(l)

def countList(arr):
	if arr == []:
		return 0
	return 1 + countList(arr[1:])

print countList(l)