def index_max():
    num_list = []
    dog = True
    while dog:
        n = int(input())

        if n == 0:
            dog = False
        else:
            num_list.append(n)

    return num_list.index(max(num_list))


print(index_max())
