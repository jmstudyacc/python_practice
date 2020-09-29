# Given two timestamps of the same day: a number of hours, minutes and seconds for both of the timestamps
# The moment of the first timestamp happened before the moment of the second one. Calculate how many seconds passed between them.
# Example Input = 1 1 1 2 2 2 | Example Output: 3661

hours1 = int(input())
minutes1 = int(input())
seconds1 = int(input())

hours2 = int(input())
minutes2 = int(input())
seconds2 = int(input())

diff_hours = hours2 - hours1
diff_mins = minutes2 - minutes1
diff_secs = seconds2 - seconds1

hours_to_secs = diff_hours * 60 *60
mins_to_secs = diff_mins * 60

total_secs = hours_to_secs + mins_to_secs + diff_secs
print(total_secs)