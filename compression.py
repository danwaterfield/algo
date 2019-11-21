
import itertools

string = "aaaabbcdddeeeefffggggggg"


def compress(string):
	if len(string) <= 1:
		return "Too short!"
	return ''.join(letter + str(len(list(group)))
		for letter, group in itertools.groupby(string))


if __name__ == '__main__':
	print(compress(string))