
# Example given 2 non-zero ints, if 1 is positive print 'YES'
# Print 'NO' otherwise
# Example: -5 10
# YES
# Example: 5 10
# NO


first_num = int(input())
second_num = int(input())

if first_num > 0 and second_num < 0:
    print('YES')
elif first_num < 0 and second_num >0:
    print('YES')
else:
    print('NO')