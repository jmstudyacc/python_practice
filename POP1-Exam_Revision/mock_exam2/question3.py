# 13198061


def test_first_most_frequent():
    assert most_frequent([1, 1, 2, 3]) == 1


def test_last_most_frequent():
    assert most_frequent([1, 2, 3, 3]) == 3


def test_mid_most_frequent():
    assert most_frequent([1, 2, 2, 3]) == 2


def test_smallest_most_frequent():
    assert most_frequent([1, 2, 3, 4, 5, 6]) == 1


def test_zero_most_frequent():
    assert most_frequent([0, 0, 1, 2]) == 0


def test_negative_most_frequent():
    assert most_frequent([-1, -1, 2, 3, 4, 5]) == -1


