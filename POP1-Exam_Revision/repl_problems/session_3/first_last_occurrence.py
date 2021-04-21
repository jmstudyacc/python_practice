def letter_index(s):
    if 'f' not in s:
        return -1
    elif s.index('f') == s.rindex('f'):
        return f'{s.index("f")}'
    else:
        return f'{s.index("f")} {s.rindex("f")}'


print(letter_index("fearful"))
print(letter_index("office"))
print(letter_index("aperitif"))
print(letter_index("window"))
print(letter_index("aaaaaafffffaaaffffffaaa"))
