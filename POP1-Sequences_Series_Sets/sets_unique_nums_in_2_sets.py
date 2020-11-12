# intersection() set method can be used here

string1 = input()
#string1 = "5 3 3 10 40"
string2 = input()
#string2 = "40 3 40 1 2"

list1 = string1.split(" ")
list2 = string2.split(" ")

set1 = set(list1)
set2 = set(list2)

print(len(set1.intersection(set2)))