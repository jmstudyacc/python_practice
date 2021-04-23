def gt_neighbour(l):
    # count holds how many satisfy requirement
    count = 0
    # holds length of the list
    lgth = len(l)
    # iterate over list from index 1 to index max-1
    for i in range(1, lgth-1):
        # if condition to check l[i-1] and l[i+1] are less than l[i]
        if l[i-1] < l[i] and l[i+1] < l[i]:
            count += 1

    return count


l1 = [1, 2, 3, 2, 8, 7, 6, 9, 5]
l2 = [1, 2, 3, 4, 5, 6, 7]
l3 = [1, 6, 3, 4, 6, 7, 3, 3, 3, 3]
l4 = [12, 34, 10, 17, 18, 19, 20]
print(gt_neighbour(l1))
print(gt_neighbour(l2))
print(gt_neighbour(l3))
print(gt_neighbour(l4))
