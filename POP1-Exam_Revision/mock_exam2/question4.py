# 13198061

def apply_functions(f, g, L):
    # returns a list of numbers
    M = []
    for i in range(len(L)):
        if L[i] < 0:
            M.append(g(L[i]))
        else:
            M.append(f(L[i]))

    return M


def double(x):
    return 2 * x


def square(x):
    return x * x

