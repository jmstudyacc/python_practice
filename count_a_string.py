
# Given a string consisting of words separated by spaces. 
# Determine how many words it has. 
# To solve the problem, use the method count.

# Example Input: 'Hello World'


"""
word = str(input())
split_word = word.split(' ')

print(len(split_word))

print(len(input().split()))
"""


def word_count(s):
  w = s.count(" ")+1
  return w