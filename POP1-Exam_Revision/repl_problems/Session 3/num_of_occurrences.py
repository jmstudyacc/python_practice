
phrase = input()

# split it to make string into list
list1 = phrase.split(" ")

# 2nd list to hold words as a check for count
list2 = []

# number of values in list
count = len(list1)

# iterate over the list of values
for i in range(len(list1)):
    # print the count of words already 
    print(list2.count(list1[i]), end=" ")
    list2.append(list1[i])