def longest_sequence(s):
    count = 1 # has to be 1 as each letter in the string appears at least 1 time
    letter = ""
    max = 0

    # iterate over the string
    for i in range(len(s)):
        # prev is the letter before current letter considered
        prev = s[i - 1]
        # if current letter considered = previous letter
        if s[i] == prev:
            # increment count by 1
            count += 1
            # if count == the maximum value
            if count == max:
                # candidate letter becomes the letter under consideration
                candidate_letter = s[i]
                # if the candidate letter is smaller than the previously saved letter
                if candidate_letter < letter:
                    # change letter to the candidate letter
                    letter = candidate_letter
            # otherwise, if the count is bigger than max
            elif count > max:
                # max equals the value of count
                max = count
                # letter is saved as the letter under consideration
                letter = s[i]

        # else, reset the count var to 1
        else:
            count = 1

    return letter, max


assert longest_sequence("dghhhmhmx") == ("h", 3)
assert longest_sequence("dhkkhhkkkt") == ("k", 3)
assert longest_sequence("abbbadddaadd") == ("b", 3)