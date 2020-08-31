# countLetters
"""
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
    uniqueLetters = 0
    for letter in letters:
        if letter in word:
            uniqueLetters +=1
    return uniqueLetters

print(unique_english_letters("Apple"))
print(unique_english_letters("mississippi"))
"""
# countX - count_char_x()

"""
def count_char_x(word, x):
    counter = 0
    for char in word:
        if char == x:
            counter +=1
    return counter
 
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
"""
# Count Multi X - count_multi_char(x)
"""
def count_multi_char_x(word, x):
  splits = word.split(x)    # Split removes the target, 'x', from the word
  print(splits)             # Print the word after split
  return(len(splits)-1)     # Count how many splits there are

print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1
"""

# Substring Between - substring_between_letters()

#def substring_between_letters(word, start, end):