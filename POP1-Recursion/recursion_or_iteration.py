# You may want to implement recursion above all else
# However be aware that recursion has a cost and may not always be as efficent as iteration
# an example is the following sets of code

format = '*' * 10
n = 3

def countUp(n):
    if n == 0:
        print(0)
    else:
        countUp(n - 1)
        print(n)


print(f'{format} THIS IS START OF RECURSIVE FUNCTION {format}')
countUp(n)
print(f'{format} THIS IS END OF RECURSIVE FUNCTION {format}\n')

# That code works and will provide a result
# Using small data points means you won't really see an issue but with a larger data set you'll see slow down
# This is because this recursion is inefficient when compared to the iterative version
# However the iterative version is more optimal as it requires less steps

def count_up(n):
    for i in range(n + 1):
        print(i)


print(f'{format} THIS IS START OF ITERATIVE FUNCTION {format}')
count_up(n)
print(f'{format} THIS IS END OF ITERATIVE FUNCTION {format}')

# If you don't believe without seeing then feel free to run it through a step-by-step analysis
# If n = 1 you will find that the recursive step has an extra 2 steps when compared to the iterative R = 12, I = 10
# At n = 2 the score becomes R = 17, I = 12
# At n = 3 the score becomes R = 22, I = 14
# Recursive lookup increases by 5 each 'n' increment, Iterative only increases by 2

