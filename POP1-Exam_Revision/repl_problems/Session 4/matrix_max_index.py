# M = matrix of numbers, list of lists
# m = number of rows in M
# n = number of columns in M

def matrix_max_index(M, m, n):
    # init the var to hold the current max int from matrix
    ele_max = 0
    idx = 0

    # iterate over the matrix
    for i in range(0, m):

        # if the value of ele_max is less than the max value of the current iteration (a list, i, in the matrix
        if ele_max < max(M[i]):

            # set ele_max to equal this value
            ele_max = max(M[i])

            # record the index it happened at
            idx = i

    # calculate the position IN the list, i, to return
    idx_pos = M[idx].index(ele_max)

    # return a tuple containing the index and the list index of the max value of the matrix
    return idx, idx_pos


M = [[0, 3, 2, 4], [2, 3, 5, 5], [5, 1, 2, 3]]
print(matrix_max_index(M, 3, 4))
M2 = [[1]]
print(matrix_max_index(M2, 1, 1))
M3 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
print(matrix_max_index(M3, 3, 5))
M4 = [[1], [2], [3], [2], [1], [2]]
print(matrix_max_index(M4, 6, 1))