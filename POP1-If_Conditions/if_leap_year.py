year_input = int(input())

if year_input % 4 == 0 and year_input % 100 != 0:
	print("LEAP")
elif year_input % 400 == 0:
	print("LEAP")
else:
	print("COMMON")