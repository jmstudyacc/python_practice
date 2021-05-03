import time
import random

def partition(xs, start, end):
    follower = leader = start
    while leader < end:
        if xs[leader] <= xs[end]:
            xs[follower], xs[leader] = xs[leader], xs[follower]
            follower += 1
        leader += 1
    xs[follower], xs[end] = xs[end], xs[follower]
    return follower


def _quicksort(xs, start, end):
    if start >= end:
        return
    p = partition(xs, start, end)
    _quicksort(xs, start, p - 1)
    _quicksort(xs, p + 1, end)


def quicksort(xs):
    _quicksort(xs, 0, len(xs) - 1)


if __name__ == "__main__":
    arr1 = [32, 73, 71, 78, 93, 30, 0, 53, 1, 74]
    arr2 = []
    for i in range(2500000):
        arr2.append(random.randrange(0, 5000000))

    start_time = time.time()
    # print(f"The list before Quicksort is applied: {arr1}")
    quicksort(arr2)
    #print(f"The list after Quicksort is applied: {arr2}")
    print(f"Program took {time.time() - start_time} seconds. ")
