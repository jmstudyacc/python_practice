
# Given an integer, print "YES" if a three digit number
# print "NO" otherwise

user_num = int(input())
user_string = str(user_num)
len_user_str = len(user_string)

if len_user_str == 3:
    print('YES')
else:
    print('NO')