def max_three(num1, num2, num3):
    max = 0             # Set max variable to an arbitrarily low number

    if num1 > max:      # if num1 is bigger than max reassign max to num1
        max = num1

    if num2 > max:      # if num2 is bigger than max reassign max to num2
        max = num2 

    if num3 > max:      # if num3 is bigger than max reassign max to num3
        max = num3
    
    return max          # return max as the outcome of function

n = max_three(-1,0,-2)
print(n)