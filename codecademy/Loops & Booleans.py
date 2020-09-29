#while True:
  #  print("Please key in four numbers: ")
  #  print("> ", end = "")
  #  s = input()
  #  num1 = int(s)
  #  print("> ", end = "")
  #  s = input()
  #  num2 = int(s)
  #  print("> ", end = "")
  #  s = input()
  #  num3 = int(s)
  #  print("> ", end = "")
  #  s = input()
  #  num4 = int(s)
  #  print("> ", end = "")
  #  total = num1 + num2 + num3 + num4
  #  print("Total: " + str(total))

# This works well for small amounts but when you need to sum larger values
# It is easier to use a loop to achieve the goal

#num = 0
#while num < 100:
#    num = num + 6
#    print(str(num))
#print("Loop complete!")

# Here the value of num starts at 0. When the value num enters the while loop
# it has 5 added to it, so the first loop is num = 0 + 5, num = 5, which is
# seen in the print out

# This iterative approach continues until the valu of num is less than 100.
# However your final result may be greater than 100 because the value of num
# is less than 100 before the addition occurs!

#https://cscircles.cemc.uwaterloo.ca/7c-loops/

#countup = 1
#while countup < 10:
#	print(countup)
#	countup = countup + 1
#print("Blast off!")

# While loops tend to work best with boolean logic - True/False
# For loops tend to work better when cycling through numbers or data
# For loops function by iterating each time similarly to the above code
# Always remember that your loops need to be started with a colon :

#for counter in range(10, 15):
#    print("counter is ", counter)

# This loop is created with the following logic
# for <variable> in range(<startValue>, tailValue>):
#       <indented block of commands called the body>
# This will continue until the variable has a a value of tailValue -1

# You can also place for loops in other for loops

#for i in range(0, 5):
#    X = 0
#    for j in range(0, 5):
#        X = (X*10)+1
#    print(X)

# You need to consider the position of the loops in a nested loop
# You can manipulate internal loops by changing something in the external loop
# See below

#print("What size triangle do you want to make?")
#n = int(input())
#for i in range(0, n):
#  X = 0
#  for j in range(0, n):
#    X = (X*10)+1
#  print(X)
#  n = n-1

# If you want to break the loop then you can use a BREAK statement
# This can be inserted with an IF statement and then the break condition created

#counter = 0
#print("Please enter some lines until you are finished.")
#while True:
#  lineIn = input()
#  if lineIn == 'END':
#    break
#  counter = counter+1
#  print('line', counter, '=', lineIn)

#n=int(input())
#counter = 1
#while counter * counter < n:
#   for counter in range(1, n):
#      a = counter * counter
#      if a >= n:
#         break
#      print(a)

# Counter here is used to track how many loops round and to provide the square numbers
# 1st loop = counters = 1 so a = 1 * 1 which is then compared against n. 2nd loop is
# a = 2 * 2 and so on until a grows bigger than the input and the loop breaks

# You can also add 'continue' to your loops to negate without ending the code
# In the code below you can see it checks for 'SKIP' and continue with the loop and not increment counter
# This is because the loop finishes when it registers 'SKIP' and does not implement the counter increase

#counter = 0
#while True:
#  lineIn = input()
#  if lineIn=='END':
#    break
#  if lineIn=='SKIP':
#    continue
#  counter = counter+1
#  print('line', counter, '=', lineIn)

  
#n=int(input())
#for a in range (0, n+1):
#    for b in range(1, n+1):
#        if a * b == n:
#            print(str(a) + " times " + str(b) + " equals " + str(n))
    
#n = int(input())
#for i in range (1, n+1):
#    if n % i == 0:
#        c = n // i
#        print(c, "times", i ,"equals", n)
        
