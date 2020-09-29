
# You are given a string.

# 1. In the first line, print the third character of this string.
# 2. In the second line, print the second to last character of this string.
# 3. In the third line, print the first five characters of this string.
# 4. In the fourth line, print all but the last two characters of this string.
# 5. In the fifth line, print all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first).
# 6. In the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).
# 7. In the seventh line, print all the characters of the string in reverse order.
# 8. In the eighth line, print every second character of the string in reverse order, starting from the last one.
# 9. In the ninth line, print the length of the given string.

# Example Input: Abrakadabra

i = input()

print(i[2])
print(i[-2])
print(i[:5])
print(i[:-2])

print(i[0::2])

print(i[1::2])

print(i[::-1])

print(i[::-2])

print(len(i))