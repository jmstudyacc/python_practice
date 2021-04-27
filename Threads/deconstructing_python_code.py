import dis


# defining some simple functions
def inc(x):
    x += 1


def unc(x):
    x -= 2


def anc(x):
    x *= 5
    x ** 2
    print(x)
    return x


print("New Function:")
# dis.dis(fn) can be used to display the steps taking to run the function
dis.dis(inc)
print("\nNew Function:")
dis.dis(unc)
print("\nNew Function:")
dis.dis(anc)