
# Let's call an integer a palindrome if it remains the same after reading its digits from right to left
# Given a four-digit integer, print "YES" if it's a palindrome 
# print "NO" otherwise. 

# Example: 1221
# Example output: YES

# Example: 1234
# Example output: NO

four_digits = int(input())

list_digits = str(four_digits)

if list_digits[0] == list_digits[-1] and list_digits[1] == list_digits[-2]:
    print('YES')
else:
    print('NO')