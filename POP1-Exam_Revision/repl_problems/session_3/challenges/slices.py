def print_slice(s):
    # print all but last two
    print(s[:-2])

    # print all but first two
    print(s[2::])

    # print all but the first two and last two
    print(s[2:-2])


s1 = "abracadabra"
s2 = "apple"
s3 = "abcd"
s4 = "ab"
print_slice(s1)
print_slice(s2)
print_slice(s3)
print_slice(s4)
