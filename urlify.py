def urlify(string):
	output = []
	for i in string:
		if i == " ":
			output.append("%20")
		else:
			output.append(i)
	return str(output)

print urlify("hello world ")