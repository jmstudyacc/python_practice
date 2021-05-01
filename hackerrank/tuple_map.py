if __name__ == '__main__':
    n = int(input())
    # map takes 2 variables and combines them
    integer_list = map(int, input().split())
    # here we print the hashed value of the map function in a tuple format
    print(hash(tuple(integer_list)))