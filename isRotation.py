def isRotation(s1, s2):
	return (len(s1) == len(s2) and s1 in s2*2)

print(isRotation("hello", "elloh"))