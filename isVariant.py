def isVariant(a, b):
	a = []
	b = []
	tempList = []
	for i in a:
		if i in a == j in b:
			tempList.append(i)
	if len(tempList) == len(a) or len(b):
		print("permutation!")
	else:
		print("Nope, different characters, sorry...")

isVariant("hello", "olleh")