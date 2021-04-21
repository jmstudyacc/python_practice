
def binary_map(f2, c1, c2):
    # returns the result of the function on pair[0] & [1] after the pair has been zipped using c1 & c2
    return (f2(pair[0], pair[1]) for pair in zip(c1, c2))


def plus(x, y):
    return x + y


def mult(x, y):
    return x * y


X = (1, 2, 3)
Y = [10, 20, 30]

Z = binary_map(plus, X, Y)
assert list(Z) == [11, 22, 33]
Z = binary_map(mult, X, Y)
assert list(Z) == [10, 40, 90]
assert hasattr(Z, '__next__')

