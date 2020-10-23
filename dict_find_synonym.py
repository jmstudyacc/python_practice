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
loop = True

synonyms = {}

while loop:
    word = input()
