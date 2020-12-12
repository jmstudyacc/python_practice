"""
Given an ordered list X of distinct ints and analogous list Y,
construct the list of all pairs (x,y) such that x is from X, y from Y, and x < y.

The resulting list must be ordered so that the pairs with the smaller x go first
and among the pairs that have the same x, the ones with the smaller y go first
(see examples in the test cases).

Important. Provide an implementation using the pattern on the right
and a list comprehension expression.
This expression must replace ... and the rest of the pattern must not be edited.

Example Input:
3 4 5 6 7
1 2 3 4 5

Example Output:
3 4
3 5
4 5

"""

Xstrs = [3, 4, 5, 6, 7]
X = [int(x) for x in Xstrs]

Ystrs = [1, 2, 3, 4, 5]
Y = [int(x) for x in Ystrs]

Z = [(x,y) for x in X for y in Y if x < y] #insert a list comprehension expression

for pair in Z: print(pair[0], pair[1])