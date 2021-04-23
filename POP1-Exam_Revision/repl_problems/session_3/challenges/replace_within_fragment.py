def replace_within(s):
    letter = "f"
    # find the first instance of 'f' & last instance of left
    lf = s.find(letter) + 1
    rf = s.rfind(letter)

    # list comprehension to take the string and make a list of chars (leaving in spaces)
    s_spl = [char for char in s]

    # iterate over the list from lf to rf
    for i in range(lf, rf):
        # if the iteration sees a 'f' replace with 'F'
        if s_spl[i] == "f":
            s_spl[i] = "F"

    # join the list together to print out a string
    return " ".join(s_spl)


print(replace_within("fifty five"))
print(replace_within("after"))
print(replace_within("fifty"))
print(replace_within(" "))
