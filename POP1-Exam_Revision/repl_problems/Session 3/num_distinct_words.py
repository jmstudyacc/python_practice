def word_count(s):
    # split string to make a list
    s1 = set(s.split(" "))

    # is the set contains '' which would be a blank space - return 0
    if '' in s1:
        return 0

    # otherwise return length of the set
    return len(s1)


print(word_count("Such a day is a bad day"))
print(word_count("one two one two three"))
print(word_count("a good pirate is a dead pirate aye"))
print(word_count("john"))
print(word_count("bravo bravo"))
print(word_count("     "))
