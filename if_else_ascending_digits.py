

# Given a three-digit integer X consisting of three different digits
# print "YES" if its three digits are going in an ascending order 
# from left to right and print "NO" otherwise
 
user_int = int(input())

user_list = str(user_int)

if user_list[0] < user_list[1] and user_list[1] < user_list[2]:
    print('YES')
else:
    print('NO')