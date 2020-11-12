"""
Input is a sequence of lines where the first line indicates which numbers are in the set initially. 
The second line indicates which numbers are removed from the set (if present). 
The third line indicates which numbers are added to the set (if not present already). 
The fourth line indicates which numbers are removed. 
The fifth indicates which numbers are added, and so on. 
The process stops when the line 

END

was entered. Print the current contents of the set in the acending order.

For example, on input:
1 9 2 8 3 7 4 6
10 7 3
5 8 
1 9
END

Output must be
2 4 5 6 8
"""
"""
loop = True

while loop:
    user_input = input()    
    if user_input != "END":
        user_list = user_input.split(" ")
        user_set = set(user_list)

        print(user_set)

        user_input = input()
        user_list = user_input.split(" ")
        user_set = set(user_list)
        user_discard = user

    #if user_input == "END":
"""

loop = True
count = 0

user_string = input()
user_set = set(user_string.split(" "))

while loop:                                             # Unknown amount of required loops, so while used
    user_choice = input()
    
    if user_choice == "END":
        end_set = list(user_set)                        # Convert the user_set variable to a list to sort
        end_set.sort()
        print(*end_set)                                 # Syntactic sugar to make converting lists easy! 
        break
    
    else:
        if count % 2 == 0:                              # Problem statement looks for EVEN + ODD so use 'count % 2' to determine
            loop_choice = user_choice.split(" ")        # Split the input taken inside the loop to remove " "
            #print(loop_choice)
            for i in range(len(loop_choice)):           # Iterate over the input 'loop_choice'
                user_set.discard(loop_choice[i])        # discard from user_set each value of loop_choice
            #print(user_set)                            # discard used as remove throws an error if element is not in the set

        elif count % 2 != 0:                            # Finding odd numbers
            loop_choice = user_choice.split(" ")
            #print(loop_choice)
            for i in range(len(loop_choice)):
                user_set.add(loop_choice[i])            # Adding not discarding
            #print(user_set)
            
    #print(user_set)
    count += 1                                      # Increment count to follow the problem statement

"""
s = input()
i = 0
cur_set = set()

while s !="END":
  
  nums_str = s.split()

  if i % 2 == 0:
    for num_str in nums_str:
      cur_set.add(int(num_str))
  else:
    for num_str in nums_str:
      cur_set.difference_update({int(num_str)})
    
  s = input()
  i+=1
  
cur_list = []
for num in cur_set:
  cur_list.append(num)
  
cur_list.sort()

for num in cur_list:
  print(num, end = " ")

"""