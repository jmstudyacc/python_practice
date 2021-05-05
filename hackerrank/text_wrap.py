import textwrap


def wrap(string, max_width):
    wrap_string = ""    # empty string to hold new value
    for i in range(0, len(string), max_width):  # step by the max_width value
        wrap_string += (string[i:(i + max_width)]) + "\n"   # add the string sliced at i to i+max_width with \n added

    return wrap_string  # return new string


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)