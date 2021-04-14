# receive a string input from user
phone_number = input()

# use list comprehension to convert from string to int
phone_number = [int(x) for x in phone_number]

# array/list holding the string names of numbers
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# loop over the list phone_number
for digit in range(len(phone_number)):
    # check the digit
    # go to numbers array
    # use checked digit for index in numbers array
    numbers_index = phone_number[digit]     # get index for the numbers list by getting the int at digit index
    print(numbers[phone_number[digit]])     # apply this int as an index into the numbers list
