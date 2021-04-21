def f(x):
    return chr(ord(x) - 32)


def stringify(val):  # higher order function
    def new_string(s):  # function that does the work
        str1 = ""
        # the variable s is provided the string by the variable f in Stringify
        for x in s:
            str1 += f(x)

        return str1

    return new_string


# F here is the function, it is a function as it has been assigned to a function
F = stringify(f)  # the variable F is assigned to the function stringify that takes f - another function

print(F("apple"))

# here G is assigned to a function
x = int(input())
G = pow(x, 2)
print(G)
