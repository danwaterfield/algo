def urlify(string):
	new_string = string.replace(" ", "%20")
	return new_string

print(urlify("John Smith Hello World"))

