"""
Given a string that may or may not contain a letter of interest. Print the index location of the first and last appearance of f. If the letter f occurs only once, then output its index. If the letter f does not occur, then print -1. 

For example, on input
fearful
output must be
0 4
"""

word = input()
target_letter = 'f'

letter_count = word.count(target_letter)

if letter_count > 1:
  print(word.find(target_letter), word.rfind(target_letter))
  
elif letter_count == 1:
  print(word.find(target_letter))
  
else:
  print(-1)

"""
s = input()
first = s.find("f")
last = s.rfind("f")
if first == last:
  print(first)
else:
  print(first, last)
"""
