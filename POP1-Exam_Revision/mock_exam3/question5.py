"""
Implement a function:

that takes two matrices of integers A and B with n rows and m columns and returns a number of positions (i,j)
where an element at this position in A is not equal to the element at this position in B.
(As usual, position (i,j) denotes i-th row and j-th column in the matrix.)
You may assume that the matrices are of the correct size and are specified in a standard way as lists of lists.
"""


def number_of_differences(n, m, A, B):
    count = 0
    # iterate over number of rows
    for i in range(n):
        # inside row iterate over values(columns) in row
        for j in range(m):
            # if the values do not match, there is the Q use case
            if A[i][j] != B[i][j]:
                # increment count by 1
                count += 1

    return count


assert number_of_differences(2, 3, [[1, 2, 3], [4, 5, 6]], [[1, 2, 4], [3, 5, 6]]) == 2
assert number_of_differences(2, 2, [[1, 2], [3, 4]], [[1, 2], [3, 4]]) == 0
