'''
def gen_board(c, r):
    board = []

    for i in range(1, c):
        row = f'{i} |', [0] * r
        board.append(row)

    for i in board:
        print(i)

gen_board(10, 10)
'''
import pytest

'''
star_format = '*' * 5
ship1 = [(1, 1), (1, 2)]
ship2 = [(2, 1), (2, 2)]
ship3 = [(3, 1), (3, 2)]
fleet = [ship1, ship2, ship3]

user_input = (1, 1)

for i in fleet:
    print(i)

# iterate over the fleet and when you find a match against the user input replace with H, H

# print("\n",fleet[0])

# if user_input == fleet[0][0]:
#    print(True)


for j in range(0, 3):  # iterate over fleet
    print(f"DEBUG MESSAGE - LIST ITEM: {j}")
    if user_input in fleet[j]:
        print(f"HIT!! fleet index {j}")
    else:
        print(f'{star_format} MISS!! {star_format} At fleet index {j}')
'''


'''def check_if_hits1(r, c, fleet):
    coord = ()
    coord += (r, c)

    for i in range(len(fleet)):
        if coord in fleet[i]:
            return True


def test_check_if_hits1():
    # add at least one test for check_if_hits by the deadline of session 7 assignment
    # provide at least five tests in total for check_if_hits by the project submission deadline

    assert check_if_hits1(r, c, fleet)

    # compare user input against list of ship tuples representing their board coords
    # if user input matches one of these board coords then it is hit
    # test will PASS if user input matches a ship board coord


r = 1
c = 1
ship1 = [(1, 1)]
ship2 = [(2, 1), (2, 2)]
fleet = [ship1, ship2]

print(check_if_hits1(1, 1, fleet))'''



'''def test_are_unsunk_ships_left1():
    # add at least one test for are_unsunk_ships_left by the deadline of session 7 assignment
    # provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
    ship1 = [(1, 1), (1, 2)]
    fleet = [ship1]
    assert(fleet != [])


ship1 = [(1, 1)]
ship2 = [(2, 1), (2, 2)]
fleet0 = [ship1, ship2]
ship_dict = {
    'ship1': [(1, 1)],
    'ship2': [(2, 1), (2, 2)],
            }


def hit(row, column, fleet):
    coord = ()
    coord += (row, column)
    fleet1 = list(ship_dict.keys())

    for i in range(0, 2):
        if coord in fleet[i]:
            for k, v in ship_dict.items():
                if coord in v:
                    ship = k

    return fleet1, ship'''


# we can store the values in a dictionary and then check against the dictionary
# that way you can also easily gather the ship type

#print(hit(1, 1, fleet0))


'''def test_hit():
    assert(hit(1, 1, fleet0)) == (fleet0, ship1)

'''
food = ['cake', 'cheese']


def add_item(n):
    food.append(n)
    return food


def test_add_item():
    add_item('pie')
    assert 'pie' in food
