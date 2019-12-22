# finds the minute at which the minute and hour hands coincide.

def findTime(hour):
	# finds angle between a minute hand and the first hour hand.
	theta = 30 * hour
	print("(", end = "")
	print((theta * 2), "/ 11) minutes")


hour = 3
findTime(hour)