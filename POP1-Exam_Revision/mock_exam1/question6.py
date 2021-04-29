def shortest_atom(original_string):
    # assign a var to begin the comparison - first letter of candidate string must match the first letter of original
    current_candidate = original_string[0]

    # j is created to hold a value used to iterate over candidate string
    j = 0

    # loop to compare original string vs candidate string
    for i in range(len(original_string)):

        # e.g. abc[i] - abc[0] = a | cand[j] - cand[0] = a | if a == a
        if original_string[i] == current_candidate[j]:
            # increment value of j by 1
            j += 1
            # if value of j matches the length of the candidate reset to 0 - captures first case
            if j == len(current_candidate):
                j = 0
        # if the characters do not match add it to the candidate string as this is a possible return string
        else:
            current_candidate = original_string[:i + 1]

    # once loop is complete, return the candidate if j is 0, else no match has been found and original string is atomic
    return current_candidate if j == 0 else original_string


assert shortest_atom("ababab") == "ab"  # must be True
assert shortest_atom("abcabc") == "abc"  # must be True
assert shortest_atom("abcab") == "abcab"  # must be True
