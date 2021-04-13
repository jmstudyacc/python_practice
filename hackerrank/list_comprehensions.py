
x = 2
y = 2
z = 2
n = 2

# list comprehension time this will print out three value i, j, k
# using those values for the iterators search in the range of the above value + 1
# that helps us actually hit 2 in the range opposed to just 0 and 1
# the conditional at the end is there to check if the three value equal n
# if they do then those values cannot be included

print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])
