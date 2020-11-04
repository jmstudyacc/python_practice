"""
Given a list of unique numbers, swap the minimal and maximal elements of this list. Print the resulting list. 

For example, on input:
5 7 3 2 1 6

Output must be
5 1 3 2 7 6 

"""
def min_max_list(l):
    split_list = l.split(" ")                   # Split the string to make a list
    min_val = min(split_list)                   # Find the minimum value in the list
    min_val_pos = split_list.index(min_val)     # Find the index of this minimum value
    max_val = max(split_list)                   # Repeat for max
    max_val_pos = split_list.index(max_val)     # As above

    """
    print(  f'\nThe input from user was {split_list}'                   # Series of print statements to check outputs
            f'\nThe Minimumum value is: {min_val}'
            f'\nThe position of the Minimum value is: {min_val_pos}'
            f'\nThe Maximum value is: {max_val}'
            f'\nThe position of the Maximum value is: {max_val_pos}'
        )
    """
    
    # Now need to swap those 2 values around
    swap_list = split_list                      # Create a new variable to not pollute other var
    swap_list[min_val_pos], swap_list[max_val_pos] = swap_list[max_val_pos], swap_list[min_val_pos]
    print(swap_list)                            # Print the swapped indexes around ^ Min swaps with Max


min_max_list(input())
