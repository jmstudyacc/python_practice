
# Given a string, cut it into two equal parts. 
# If the length of the string is odd, leave the middle character within the first chunk, 
# so that the first string contains one more character than the second. 
# Now print a new string on a single row with the first and second halves swapped: second half first and the first half last.

# Can you solve it without using if?

# Example Input: Qwerty

"""
i = 'Z'

ilen = len(i)

while ilen == 1:
    print(i)
    break

while ilen % 2 == 0:
    evlen = ilen //2
    print(i[-evlen:]+i[:evlen])
    break

while ilen % 2 != 0 and ilen != 1:
    oddlen = int(ilen / 2 )
    print(str(i[-oddlen:])+i[:oddlen+1])
    break
"""

s = input()
mid = (len(s) + 1) // 2
print(s[mid:] + s[:mid])