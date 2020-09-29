
# Given a string in which the letter h occurs at least twice. 
# Remove from that string the first and the last occurrence of the letter h, as well as all the characters between them

# Example Input: In the hole in the ground there lived a hobbit

words = input()

first_h = words.find('h')
last_h = words.rfind('h')

list_words = list(words)

		
del list_words[first_h:last_h+1]

string_words = ''.join(list_words)
print(string_words)


# Reversing
# Given a string in which the letter h occurs at least twice, 
# Reverse the sequence of characters enclosed between the first and last occurrences of it

# Example Input: In the hole in the ground there lived a hobbit

words = input()

first_h = words.find('h')

last_h = words.rfind('h')

list_words = list(words)

old_words = words[first_h+1:last_h]
#print(old_words)

new_words = ''.join(reversed(words[first_h+1:last_h]))
#print(new_words)

print(words.replace(old_words, new_words))