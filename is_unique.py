def isUnique(string):
	tempBuffer = []
	for letter in string:
		if not letter in tempBuffer:
			tempBuffer.append(letter)
	if len(tempBuffer) == len(string):
		return "unique characters!"
	else:
		return "not unique!"

print(isUnique("abcde"))
