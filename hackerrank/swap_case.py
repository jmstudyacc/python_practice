def swap_case(s):
    """
    Below is 1 way to tackle this if you do not have access to the built-in libraries
    ------
    swap_string = ""
    for i in s:
        if i.islower():
            swap_string += i.upper()
        else:
            swap_string += i.lower()

    return swap_string
    """
    # uses the builtin swapcase() library
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)