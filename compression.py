import collections
import json

string = "aaaabbcdddeeeefffggggggg"
count = collections.Counter()

def compressString(string):
	string_list = []
	for char in string:
		string_list.append(char)
		count[char] += 1
	
	for k, v in count.items():
		print k + str(v)
		


print(compressString(string))
