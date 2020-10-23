a1 = [4, 6, 10, 20, 45]
a2 = [3, 6, 9, 10]

new_list = []


for i in range(0, len(a1)):
    for j in a2:
        if a1[i] == j:
            new_list.append(a1[i])
            break

for i in range(len(new_list)):
    a1.remove(new_list[i])

print(a1)


"""
def ascending_list(array):                                          # Function to sort the array in ASCENDING order 
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]

    return array


def compare_lists(a1, a2):
    #a1 = [1, 6, 10, 23, 51]
    #a2 = [3, 6, 9, 17, 20]

    a1_asc = ascending_list(a1)
    a2_asc = ascending_list(a2)

    new_list = a1
    
    len_a3 = 0
    len_a1 = len(a1)
    len_a2 = len(a2)

    #print("Length of A1 is: ",len_a1)
    #print("Length of A2 is: ",len_a2)

    if len_a1 > len_a2:
        len_a3 = len_a2
    else:
        len_a3 = len_a1

    #print(len_a3)

    for i in range(len_a1):
        for j in a2_asc:
            print(j, end=" ")
            if a1_asc[i] == a2_asc:
                print("YES - NUMBER IS",a1_asc[i])

    for i in range(len_a3):
        if i < len_a3:
            if a1_asc[i] == a2_asc[i]:
                #print(a1_asc[i])
                new_list.remove(a1_asc[i])

    #print(new_list)

compare_lists(a1, a2)
"""
