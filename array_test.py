A = [50, 20, 30, 10, 40]


def ascending_list(array):                                          # Function to sort the array in ASCENDING order 
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
                #print(f'Min_idx changes to: {min_idx}')

        array[i], array[min_idx] = array[min_idx], array[i]

    print("\nSorted array") 
    for i in range(len(array)): 
        print(f'{array[i]}')  
    
    return array

def descending_list(array):                                         # Function to sort the array in DESCENDING order
    for i in range(len(array)):                                     # 1st For loop iterating over the provided array until the total number of elements in array 
        min_idx = i                                                 # Assign 'i' value to min_idx to be used as comparison later
        for j in range(i+1, len(array)):                            # 2nd For loop starting at 'i + 1', iterating always from the value ahead of 1st For loop
            if array[min_idx] < array[j]:                           # If value in array at 'min_idx' position is less than value in array at 'j' position
                min_idx = j                                         # Change 'min_idx' value to 'j'
                #print(f'Min_idx changes to: {min_idx}')

        array[i], array[min_idx] = array[min_idx], array[i]         # At end of 2nd For loop swap the value of array[i] and array[min_idx]

    print("\nSorted Array")                
    for i in range(len(array)): 
        print(f'{array[i]}')  
    print(array)

descending_list(A)