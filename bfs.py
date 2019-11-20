"""
implementation of bfs on graph from grokking algorithms
"""
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
	return name[-1] == 'm' #a mango seller is defined as any person whose name ends with 'm'

def search(name):
	search_queue = deque()
	search_queue += graph["you"]
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person_is_seller(person):
				print(person + " is a mango seller")
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False

print(search("c"))