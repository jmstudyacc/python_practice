"""
Expression of List syntax:
[ expression for item in list ]
    |             /        \
[ letter  for  letter in 'human']
"""


h_letters = [ letter for letter in 'human' ]
print(h_letters)

a_letters = [ letter for letter in 'animal' ]
print(a_letters)

# below shows how to do a logical AND with Python list comprehension
divisible_by_ten = [ number for number in range(1, 101) if number % 3 == 0 if number % 5 == 0]
print(divisible_by_ten)

# below shows how you take a matrix and transpose using list comprehension
matrix = [[1,2],[3,4],[5,6],[7,8]]
transposed_matrix = [[row[i] for row in matrix] for i in range(1)]
print("By using '1' as the range we only print the first row")
print(transposed_matrix)

print("\nBy using '2' as the range we print both rows")
transposed_matrix = [[row[i] for row in matrix] for i in range(2)]
print(transposed_matrix)

print("\nBy changing the beginning of the range command we can print out only the 2nd row")
transposed_matrix = [[row[i] for row in matrix] for i in range(1, 2)]
print(transposed_matrix)

# nested loops in list comprehension work from right to left -
# this is how the [i] is defined as 1 or 2 by the loop

x = [1, 9, 3, 4]
y = [5, 6, 7, 8]
z = ['a', 'b', 'c', 'd']

# for loop to combine the 2 lists using zip
for a, b in zip(x, y):
    print(a, b)

print('\n')

# list comprehension to print out the zip result of xy
[ print(x, y) for x, y in zip(x, y) if x < y ]