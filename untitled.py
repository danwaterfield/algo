#implementing an unsorted linked list in python

class linkedListNode:
	def __init__(self, value, nextNode=None):
		self.value = value
		self.nextNode = nextNode

node1 = linkedListNode("1")
node2 = linkedListNode("2")
node3 = linkedListNode("3")
node4 = linkedListNode("4")
node5 = linkedListNode("4")
node6 = linkedListNode("5")

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5
node5.nextNode = node6


currentNode = node1
while True:
	print currentNode.value, "->", 
	if currentNode.nextNode is None:
		print "None"
		break 
	currentNode = currentNode.nextNode


class linkedList:
	def __init__(self, head=None):
		self.head = head

	def insert(self, value):
		node = linkedListNode(value)
		if self.head is None:
			self.head = node
			return

	currentNode = self.head
	while True:
		if currentNode.nextNode is None:
			currentNode.nextNode = None
			break 
		currentNode = currentNode.nextNode