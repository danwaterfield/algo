def compressMe(string):
	temp = {}
	result = ''
	for i in string:
		if i in temp:
			temp[i] = temp[i]+1
		else: 
			temp[i] = 1
	for k, v in temp.items():
		result += str(k) + str(v)
#checks if the compression shortens the length of the string, and returns the original string if each element
#in the original string is unique
	if len(temp) == len(string):
		return string
	else:
		return result

print compressMe('aabbccd')