
# this program calculates the edit distance between two strings, s1 and s2, and tells the user how many steps would be required
# to change s1 to s2. Would be nice to take user input... 

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 
            deletions = current_row[j] + 1       
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

result = levenshtein("uwu", "uwu222222")


if int(result) == 0: 
    print "no difference"
elif int(result) == 1:
    print "One away"
elif int(result) >= 2:
    print "Edit distance is %d" %int(result) 


