def isSubstring(s1, s2):
	size1 = len(s1)
	size2 = len(s2)
	temp = ''

	if size1 != size2:
		return 0

	temp = s1 + s1

	if (temp.count(s2)> 0):
		return 1
	else:
		return 0

s1 = 'daa'
s2 = 'ada'

def testCase():
	if isSubstring(s1, s2):
		print "Rotation detected"
	else:
		print "No rotation detected"

print testCase()