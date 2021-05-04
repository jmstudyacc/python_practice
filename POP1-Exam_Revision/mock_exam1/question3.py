# 13198061

def swap_min_max(L):
    # maximal and minimal numbers in list are swapped
    # returns a new list
    # if there are multiple max numbers, swap the last max number with the min number
    # if there are multiple min numbers, swap the last min number with the max number
    # if there are both, swap the last max with the last min
    pass


def test_swap_ordered_min_max():
    assert swap_min_max([1, 2, 3, 4, 5]) == [5, 2, 3, 4, 1]


def test_swap_unordered_min_max():
    assert swap_min_max([3, 5, 4, 1, 2]) == [3, 1, 4, 2, 5]


def test_swap_multiple_min():
    assert swap_min_max([1, 1, 1, 4, 5]) == [1, 1, 5, 4, 1]


def test_swap_multiple_max():
    assert swap_min_max([1, 2, 3, 5, 5]) == [5, 2, 3, 5, 1]


def test_swap_multi_max_min():
    assert swap_min_max(1, 1, 2, 3, 4, 5, 5) == [1, 5, 2, 3, 4, 5, 1]


def test_swap_zero_min_max():
    assert swap_min_max([0]) == [0]
