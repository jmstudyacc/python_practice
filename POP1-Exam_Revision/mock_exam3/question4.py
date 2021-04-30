def f(L):
    X = [x for x in L for y in L if x + y == 10]
    if (len(X)) > 0:
        return True
    else:
        return False


print(f([-5, 5]))


# X is not a list, it is a generator and cannot have length - rewrite:
# [x for x in L for y in L if x + y == 10]

# Print statements are not the same as Return statements - rewrite:
"""
if (len(X)) > 0:
    return True
else:
    return False
"""