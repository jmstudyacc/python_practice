"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position
print: Print the list
remove e: Delete the first occurrence of integer
append e: Insert integer  at the end of the list
sort: Sort the list
pop: Pop the last element from the list
reverse: Reverse the list

"""

if __name__ == '__main__':
    l1 = []
    N = int(input())
    for i in range(N):
        u_input1 = input().split()
        inst = u_input1[0]

        if inst == 'insert':
            x = int(u_input1[1])
            y = int(u_input1[2])
            l1.insert(x, y)

        elif inst == 'remove':
            x = int(u_input1[1])
            l1.remove(x)

        elif inst == 'append':
            x = int(u_input1[1])
            l1.append(x)

        elif inst == 'sort':
            l1.sort()

        elif inst == 'pop':
            l1.pop()

        elif inst == 'reverse':
            l1.reverse()

        elif inst == 'print':
            print(l1)

        else:
            print("Error: Incorrect instruction provided.")

"""
for _ in range(int(input())):
    command, *value = input().split()
    if command == 'print':
        print(lis)
    else:
        getattr(lis,command)(*(map(int, value)))
"""