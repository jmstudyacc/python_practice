def word_count(s):
    # python, when splitting string call SPLIT on the string
    # print(" ".join(l1)) - joins a list together to make a String
    l1 = s.split(" ")
    return len(l1)


print(word_count("john"))
