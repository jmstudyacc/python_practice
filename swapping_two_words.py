
# Given a string consisting of exactly two words separated by a space. 
# Print a new string with the first and second words swapped: the second word is printed first. 
# Consider all adjacent non-space characters a single word.

# Can you solve it without using if-else and loops?

two_words = input()

split_words = two_words.split()

target_list = [] 
target_list.append(split_words[1])
target_list.append(split_words[0])
print(target_list)