"""
Given two lists of numbers, print the numbers that are in the first list but are not in the second. 
Print those numbers in the ascending order. (You can assume that the numbers in each of the two lists do not repeat.)

For example, on input
20 4 45 6 10
9 10 6 3

Output must be
4 20 45

"""

# Sort the lists into ascending
# Make Lists into Sets
# Use the built-in difference() method for Sets

def string_to_array(l1, l2):
    split_string1 = l1.split(" ")
    array_l1 = []
    array_l1_len = len(split_string1)

    split_string2 = l2.split(" ")
    array_l2 = []
    array_l2_len = len(split_string2)

    for i in range(0, array_l1_len):
        number = int(split_string1[i])
        array_l1.append(number)

    for i in range(0, array_l2_len):
        number = int(split_string2[i])
        array_l2.append(number)

    return array_l1, array_l2

def ascending_list(array1, array2):                                          # Function to sort the array in ASCENDING order 
    for i in range(len(array1)):
        min_idx = i
        for j in range(i+1, len(array1)):
            if array1[min_idx] > array1[j]:
                min_idx = j

        array1[i], array1[min_idx] = array1[min_idx], array1[i]

    for i in range(len(array2)):
        min_idx2 = i
        for j in range(i+1, len(array2)):
            if array2[min_idx2] > array2[j]:
                min_idx2 = j

        array2[i], array2[min_idx2] = array2[min_idx2], array2[i]

    #print ("\nSorted array") 
    #for i in range(len(array)): 
    #   print(f'{array[i]}', end= ' ')
    return array1, array2

def compare_lists(array1, array2):
    array_string = string_to_array(array1, array2)
    #print(array_string)
    
    ascending_array = ascending_list(array_string[0], array_string[1])
    #print(ascending_array)
    
    a1 = array_string[0]
    a2 = array_string[1]
    new_list = array_string[0]
    
    #print(a1)
    #print(a2)
    #print(new_list)

    len_a1 = len(a1)
    len_a2 = len(a2)

    #print("Length of A1 is: ",len_a1)
    #print("Length of A2 is: ",len_a2)

    #print(len_a3)

    new_list = []

    for i in range(0, len(a1)):
        for j in a2:
            if a1[i] == j:
                new_list.append(a1[i])
                break
    
    for i in range(len(new_list)):
        a1.remove(new_list[i])

    return a1

#compare_lists(input(), input())
print(compare_lists("20 4 45 6 10", "9 10 6 3"))
