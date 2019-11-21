def isPalindrome(s1, s2):
	if s1[::-1] == s2:
		return True
	else: 
		return False


print(isPalindrome('hello', 'olleh'))