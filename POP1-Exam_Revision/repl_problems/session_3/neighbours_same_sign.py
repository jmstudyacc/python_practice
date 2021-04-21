def neighbours_same_sign(l):
    for i in range(len(l) - 1):
        if l[i] < 0 and l[i + 1] < 0:
            return f"{l[i]} {l[i + 1]}"

        elif l[i] >= 0 and l[i + 1] >= 0:
            return f"{l[i]} {l[i + 1]}"

    return " "


list1 = input().split(" ")
list1 = [int(i) for i in list1]
print(neighbours_same_sign(list1))
