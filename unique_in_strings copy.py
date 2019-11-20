"""
short program to check unique chars present in 2 strings
written as part of codecademy python3 course

"""

def common_letters(string_one, string_two):
  new_list = []
  for i in string_one:
    for j in string_two:
      if i not in new_list:
        if i == j:
          new_list.append(i)
  return new_list


print common_letters('hello', 'world')