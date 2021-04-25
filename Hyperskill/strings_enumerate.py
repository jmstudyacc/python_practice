
# get input from user and split it to make list
input1 = input().split()

# input from user for target string number
num = input()

# if the number is in the input then true
if num in input1:
    # use enumerate over the list and use i (track index) and _ as a throw away to track
    for i, _ in enumerate(input1):
        # if the throw away matches num then print index with a " " at the end
        if _ == num:
            print(i, end=" ")

# if not in list then bailout
else:
    print("not found")
