# multiple versions of the algorithm
# this version will pick the 'middle' element of the 'array'
# quicksort requires a partition function as well as the sort function
import random
import time

def quicksort(arr, left, right):
    # print(f"Current left value: {left}")
    # print(f"Current right value: {right}")
    # base case to exit the recursive lookup
    if left >= right:
        return

    pivot = arr[(left + (right - left) // 2)]
    # print(f"Current pivot value: {pivot}")

    # partition array around this pivot point - value of left is updated with each recursion
    index = partition(arr, left, right, pivot)
    # print(f"Current index value: {index}")

    # print(f"Current list during Quicksort: {arr}\n")
    # recursive quicksort call on the array with the lower (left) and upper (mid -1)
    quicksort(arr, left, index - 1)

    # recursive quicksort call on the array with the index (pivot) and end of array (len - 1)
    quicksort(arr, index, right)


def partition(arr, left, right, pivot):
    # while left (lower) is less than right (upper) continue the loop
    while left <= right:
        # while the value at index left of the array is less than pivot continue moving 'right'
        while arr[left] < pivot:
            left += 1

        # contraflow to above
        while arr[right] > pivot:
            right -= 1

        # if both while loops have been escaped it is time to swap values at the specific array indexes
        # value of left & right are swapped and left & right are incre/decremented appropriately
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # if outer while loop has escaped then the left value needs to be returned
    return left


if __name__ == "__main__":

    arr2 = [32, 73, 71, 78, 93, 30, 0, 53, 1, 74]
    arr1 = []
    for i in range(2500000):
        arr1.append(random.randrange(0, 5000000))
    start_time = time.time()
    # print(f"The list before Quicksort is applied: {arr1}")
    quicksort(arr1, 0, len(arr1) - 1)
    # print(f"The list after Quicksort is applied: {arr1}")
    print(f"Program took {time.time() - start_time} seconds. ")
