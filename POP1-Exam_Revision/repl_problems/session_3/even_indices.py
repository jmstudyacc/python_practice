def even_indices(s):
    list1 = s.split(" ")
    for i in range(len(list1)):
        if i % 2 == 0:
            print(list1[i], end=" ")


even_indices("13 4 23 4 5 6")
print("\n")
even_indices("10 9 8 7 6 5 4 3 2 1")
print("\n")
even_indices("35")
