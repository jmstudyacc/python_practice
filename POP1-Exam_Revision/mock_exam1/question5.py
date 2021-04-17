def balance(init_sum, int_rate, tfl, tax_rate, M):
    # s is the amount of money first put in
    s = init_sum

    # create a loop to go from 0 month to M month
    for i in range(M):

        # interest rate is calculated as int_rate * s
        interest = (int_rate / 100) * s

        # if s is larger than the tax free allowance
        if s > tfl:
            # tax equals tax_rate% * total balance minus the allowance
            tax = (tax_rate / 100) * (s - tfl)
        else:
            # otherwise there is no tax to pay this month
            tax = 0

        # positioning of this line is important!!
        # s is reassigned IN THE LOOP - to equal the below
        s = s + interest - tax

    # once the loop ends the new value of s is returned
    return s


print(balance(10000, 1, 20000, 1, 2))  # must be approximately 10201
print(balance(25000, 2, 20000, 1, 2))  # must be approximately 25904.5
print(balance(19800, 2, 20000, 1, 2))  # must be approximately 20597.96
