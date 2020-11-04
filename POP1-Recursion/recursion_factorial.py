

def fac(num):
    if num == 1:
        return 1

    else:       # Time to write the reductive 
        fac_num_minus_1 = fac(num-1)    # Call the function on (n-1)
        result = num * fac_num_minus_1
        return result

print(fac(3))