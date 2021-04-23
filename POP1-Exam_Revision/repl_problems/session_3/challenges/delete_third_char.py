def third_char(s):
    # create a new variable to store new info
    result = ""

    # iterate from 0 to the length of the String
    for i in range(0, len(s)):
        # not 0 then add the letter to the new variable
        if i % 3 != 0:
            result += s[i]

    print(result)


third_char("abracadabra")
