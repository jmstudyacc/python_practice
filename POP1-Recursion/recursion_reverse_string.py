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

    else:
        return rev_string(s[1:]) + s[0]
        # return s[-1] + rev_string(s[:-1])           # rev_string(s[:-1]) removes 1 value on each recursion and assigns to s - do s[:-2] to see the difference
                                                    # the function returns the value at s[-1]

print(rev_string("abcb"))

"""
a = input()

if a < 1:
    print(a)

else:

print(a[::-1])

"""