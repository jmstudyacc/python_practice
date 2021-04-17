def replace(s):
    changed = list(s)
    for i in range(0, len(changed)):
        if 'a' <= s[i] <= 'z':
            changed[i] = s[i].upper()
        else:
            changed[i] = s[i]
    return "".join(changed)


print(replace("'ABe'"))

# error 1 - strings are immutable | typecast into list
# error 2 - minus 1 on length, last element not being changed | remove minus 1 from the length condition
# error 3 -
