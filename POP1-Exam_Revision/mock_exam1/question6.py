def shortest_atom(original_string):
    current_candidate = original_string[0]
    j = 0
    for i in range(len(original_string)):
        if original_string[i] == current_candidate[j]:
            j += 1
            if j == len(current_candidate):
                j = 0
        else:
            current_candidate = original_string[:i + 1]

    return current_candidate if j == 0 else original_string


assert shortest_atom("ababab") == "ab"  # must be True
assert shortest_atom("abcabc") == "abc"  # must be True
assert shortest_atom("abcab") == "abcab"  # must be True
