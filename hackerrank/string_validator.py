if __name__ == '__main__':
    # get input from user
    s = input()
    # loop over the list of methods
    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper, str.istitle]:
        # Return True if any element of the iterable is true. If the iterable is empty, return False
        print(any(method(c) for c in s))    # the string, s, is checked against each method above
