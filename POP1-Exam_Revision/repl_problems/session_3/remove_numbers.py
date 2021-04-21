def remove_numbers():
    s1 = set()
    dog = True
    count = 1

    while dog:
        inp1 = input().split(" ")

        if inp1 == ['END']:
            break

        if len(s1) == 0:
            for i in range(len(inp1)):
                if inp1[i] == "":
                    continue
                else:
                    s1.add(inp1[i])
            count += 1

        elif count % 2 == 0:
            for i in range(len(inp1)):
                if inp1[i] == "" or inp1[i] not in s1:
                    continue
                else:
                    s1.remove(inp1[i])
            count += 1

        else:
            for i in range(len(inp1)):
                if inp1[i] == "":
                    continue
                else:
                    s1.add(inp1[i])
            count += 1

    result = list(s1)
    result.sort()

    return f'{" ".join(result)}'


print(remove_numbers())
