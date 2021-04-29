def add_row(A, v, n):
    x = tuple(v)
    x = list(x)
    A += [x] * n

A = [[1, 2], [3, 4]]
v = [5, 6]
add_row(A, v, 2)
v[0] = 0
print(A)

# The result will be [[1, 2], [3, 4], [0, 6], [0, 6]],
# while the expected result
# is [[1, 2], [3, 4], [5, 6], [5, 6]].

"""
Program does not return the expected result because v[0] = 0 causes the result to be rewritten to [0, 6] * n
You need to create a new variable to store the tuple version of v - immutable, cast back to list and * by n
"""