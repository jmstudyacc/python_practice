"""
Implement a function rev_string(s) that given a string s returns it reversed. 

Do not use any standard string or list functions or loops. Use the following idea to implement the function recursively:

- if the string is empty, its reverse is the empty string
- otherwise, the reverse of the string is a concatenation of the string without the first symbol reversed and the first symbol

For example, the result of:

print(rev_string("abcb"))

Must be:

bcba
"""
def rev_string(s):
    if len(s) == 0:
        return s




print(rev_string("abcb"))
