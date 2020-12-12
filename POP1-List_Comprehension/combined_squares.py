"""Given lists of integer objects
X = [x1,.., xn] and Y = [y1, ..., yn],
produce an iterator to the sequence(x1 * x1, y1), (x2 * x2, y2), ...(xn * xn, yn).

Provide an implementation using the pattern on the
right and a zip expression.This expression must replace... and the rest
of the pattern must not be edited.

For example:

Input:
-----
1 2 3
5 6 7

Output:
------
1 5
4 6
9 7

"""

X = [1, 2, 3]
Y = [5, 6, 7]

it_squared_mapping = [((x * x), y) for x,y in zip(X, Y)] #insert a zip expression here

# model answer = zip((x**2 for x in X), Y)

for x in it_squared_mapping: print(x[0], x[1])