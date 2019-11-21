from collections import deque
def rotateString(string):
	string = deque(string)
	string.rotate(1)
	print ''.join(string)

rotateString("helloworld")
