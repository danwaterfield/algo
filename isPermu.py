def isPermutation(s1, s2):
	
	tempBuffer = []

	if len(s1) != len(s2):
		print "They're not even the same length..."

	
	for char in s1:
		for letter in s2:
			if char == letter:
				tempBuffer.append(char)

	if len(s1) == len(tempBuffer):
		print "permutation!"

	elif len(s1) != len(tempBuffer):
		 print "not permutation!"

print(isPermutation("Hi", "hihi"))