
# easy, naive... and slow. Good for queries in the hundreds of possible strings. 

# Anything bigger, use aho-corasick.

import re

def match(text, pattern):
	if re.search(pattern, text):
		print('woohoo, a match!')
	else:
		print('Sorry, no match')


print(match("Hello there, I am using Python", "Py"))


