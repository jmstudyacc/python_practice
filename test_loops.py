

def list_differences(l1, l2):
    print(l1)
 

#list_differences([1, 2, 3], [3, 2, 1])

names = list(input())
format_names = []

for i in range(0, len(names)):
    #print(f"This is iteration {i}")
    if names[i] != ' ':
        format_names.append(names[i])

print(format_names)
sorted_list = []
format_names_len = len(format_names)

for i in range(0, len(format_names)):
    if i+1 >= format_names_len:
        break
    else:
        print(f"\nThis is ITERATION: {i}")
        print(f"This is iteration value: {format_names[i]}")
        print(f"This is the next iteration value: {format_names[i+1]}\n")
        #print(f"\nThe value being observed in this iteration is: {format_names[i]}")
    
        if format_names[i] < format_names[i+1]:
            sorted_list.append(format_names[i])
            print(sorted_list)

    #for j in range(0, len(format_names)):
        #print(f"\nThis is the iteration number: {i}")
        #print(f"\nThe value being observed in this iteration is: {format_names[j]}")
