def recursive_reverse(s):
    # if the string is empty retrn nothing
    if len(s) == 0:
        return ""
    # recurse from the index 1 to the end and add the first element to end of word
    else:
        return recursive_reverse(s[1:]) + s[0]


assert recursive_reverse("abcb") == "bcba"
assert recursive_reverse("") == ""
assert recursive_reverse("a") == "a"
assert recursive_reverse("abcdefghijkl") == "lkjihgfedcba"
