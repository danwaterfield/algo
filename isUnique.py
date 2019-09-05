def isUnique(user_input):
	compare = []
	for i in user_input:
		if i in user_input not in compare:
			compare.append(i)
	if len(user_input) != len(compare):
		print "not unique!"
	else:
		print "sorry, not unique"
isUnique("uwuwhatisthis")