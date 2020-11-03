"""
You are given a dictionary consisting of word pairs. 
Every word is a synonym the other word in its pair. 
All the words in the dictionary are different.

First line of the input specifies how many word pairs will follow. 
After the dictionary there is one more word given. Find a synonym for this word.

Hint. To solve the problem quickly, use dictionaries.

For example, on input:
3
water liquid
fire heat
python java
fire

Output must be:

heat
"""
word_list = []
num_entries = int(input())

for i in range(0, num_entries):
    user_word = input().split()         # Splits the input by " " and makes it a list
    word_list.append(user_word)         # print the output

dict_words = dict(word_list)

synonym_lookup = input()

for key in dict_words:                  # loop over the keys in the dictionary        
    if key == synonym_lookup:           # if you find a key matching the input
        print(dict_words[key])          # print the value from the dictionary matching the value of key in the loop
