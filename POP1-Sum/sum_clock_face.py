n = int(input())

mins_hour = 60

multi_hours = n // 60       # How many hours have passed based on user input

#print(multi_hours)

num_mins = n - (mins_hour * multi_hours)    # Determine the number of minutes by finding minutes value of the hours passed

#print(num_mins)

if multi_hours >= 0 and multi_hours < 24:   # If statement used to test and catch any error input
	print(multi_hours,num_mins)
	