def fun(L1, L2):
    if L1 == [] and L2 == []:
        return []
    else:
        return [(L1[0] + L2[0]) / 2] + fun(L1[1:], L2[1:])


L1 = [1, 2, 3, 4, 5]
L2 = [6, 7, 8, 9, 10]

print(fun(L1, L2))

# Function adds value at L1[0] and L2[0] then divides by 2. This procedure continues until the lists are empty.
# Once lists are empty recursive base clause is hit and new list is returned