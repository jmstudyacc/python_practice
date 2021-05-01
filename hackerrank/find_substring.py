def count_substring(string, sub_string):
    total = 0
    str_len = len(string)
    sub_len = len(sub_string)
    # loop over the string length
    for i in range(str_len):
        # the slice will be current iteration to  length of target substring
        skip = string[i:i+sub_len]
        # if substring is in that slice increment total
        if sub_string in skip:
            total += 1

    return total


if __name__ == '__main__':
    # string = input().strip()
    string = "ABCDCDC"
    # sub_string = input().strip()
    sub_string = "CDC"

    count = count_substring(string, sub_string)

    print(count)
