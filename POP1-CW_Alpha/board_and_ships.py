from random import randint


# TOO MANY IF STATEMENTS
# TOO MANY NESTED IF STATEMENTS
# TOO MANY CONDITIONS TO CHECK AGAINST

# TO DO:
# - Error Handling for User Inputs
# - Ship placement error logic, not currently working?


def submarine_place():
    while True:
        rand_x = randint(2, 11)
        rand_y = randint(2, 11)
        coord1 = (rand_x, rand_y)

        if rand_x or rand_y == 9:
            if game_board[rand_x][rand_y] == '.':
                if game_board[rand_x - 1][rand_y] and game_board[rand_x - 1][rand_y - 1] and game_board[rand_x][
                    rand_y - 1] == '.':
                    game_board[rand_x][rand_y] = 'S'
                    break
                else:
                    print("NOT SUITABLE TO PLACE")
                    continue

        elif game_board[rand_x][rand_y] == '.':
            if game_board[rand_x + 1][rand_y + 1] and game_board[rand_x + 1][rand_y] and game_board[rand_x + 1][
                rand_y - 1] and game_board[rand_x][rand_y - 1] and game_board[rand_x][rand_y + 1] == '.':
                game_board[rand_x][rand_y] = 'S'
                break
            else:
                print("NOT SUITABLE TO PLACE")
                continue

    return [coord1]


def destroyer_place():
    while True:
        rand_x = randint(2, 10)
        rand_y = randint(2, 10)
        coord1 = (rand_x, rand_y)
        coord2 = (rand_x + 1, rand_y)

        if game_board[rand_x][rand_y] == '.':
            if game_board[rand_x + 1][rand_y + 1] and game_board[rand_x][rand_y + 1] == '.':
                game_board[rand_x][rand_y] = 'D'
                game_board[rand_x + 1][rand_y] = 'D'
                break

    return [coord1, coord2]


def cruiser_place():
    while True:
        rand_x = randint(2, 9)
        rand_y = randint(2, 9)

        coord1 = (rand_x, rand_y)
        coord2 = (rand_x, rand_y + 1)
        coord3 = (rand_x, rand_y + 2)

        # this increments 'y' so this is a
        if game_board[rand_x][rand_y] and game_board[rand_x][rand_y + 1] and game_board[rand_x][rand_y + 2] == '.':
            game_board[rand_x][rand_y] = 'C'
            game_board[rand_x][rand_y + 1] = 'C'
            game_board[rand_x][rand_y + 2] = 'C'
            break

    return [coord1, coord2, coord3]


def battleship_place():
    while True:
        rand_x = randint(2, 8)
        rand_y = randint(2, 8)

        coord1 = (rand_x, rand_y)
        coord2 = (rand_x + 1, rand_y)
        coord3 = (rand_x + 2, rand_y)
        coord4 = (rand_x + 3, rand_y)

        if game_board[rand_x][rand_y] == '.':
            game_board[rand_x][rand_y] = 'B'
            game_board[rand_x + 1][rand_y] = 'B'
            game_board[rand_x + 2][rand_y] = 'B'
            game_board[rand_x + 3][rand_y] = 'B'
            break

    return [coord1, coord2, coord3, coord4]


def blank_board(m, n):
    header_row = [[' ', '|', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['-'] * 13]
    game_board.extend(header_row)
    for z in range(m):
        row = [str(z)] + ['|'] + ['.'] * n
        # row = ['.'] * n
        game_board.append(row)

    print('{:s}'.format('\u0332'.join("\nThe empty board: \n")))
    [print(" ".join(game_board[i])) for i in range(len(game_board))]


def show_grid(board):
    # this is not efficient - how to keep the last grid and only change the new changes?
    print("\n" + "*" * 20)

    # \u0332 underlines the string that joins
    print('{:s}'.format('\u0332'.join("\nThe updated board: \n")))

    # prints the board out
    [print(" ".join(game_board[i])) for i in range(len(game_board))]


# [battleship_place() for battleship in range(1)]
# [cruiser_place() for cruiser in range(2)]
# [destroyer_place() for destroyer in range(3)]
# [submarine_place() for submarine in range(4)]


def randomly_place_ships():
    for ship in range(1, 3):
        submarine_entry = submarine_place()
        ship_list.append(submarine_entry)
        ship_fleet['sub' + str(ship)] = submarine_entry

    for ship in range(1, 2):
        destroyer_entry = destroyer_place()
        ship_list.append(destroyer_entry)
        ship_fleet['destroyer' + str(ship)] = destroyer_entry


# for i in range(1, 3):
# cruiser_entry = cruiser_place()
# ship_list.append(cruiser_entry)
# ship_fleet['cruiser'+str(i)] = cruiser_entry

# for i in range(1, 2):
# ship_fleet['battleship' + str(i)] = battleship_place()
# ship_list.append(battleship_place())

# check to see if the dictionary was successfully populated
# for item in ship_fleet:
#    print(item, ship_fleet.get(item))   # print the item currently iterated & get the value for the item


def check_if_hits(row, column, fleet):
    try:
        row = int(row)
        column = int(column)
        fleet = ship_list

        if row < 0 or row > 9 or column < 0 or column > 9:
            print("ERROR: You selected values outside of the gameboard, please try again.")

        else:
            user_x = row + 2
            user_y = column + 2
            shot = (user_x, user_y)

            # Python list comp to see if the input is in ship_list
            val = shot in [coord for ship in fleet for coord in ship]

            # if it is print that it hits and enter the list to remove the element
            if val:
                print("THAT'S A HIT!!!")
                # for i in range(len(ship_list)):
                #    if shot in ship_list[i]:
                #        ship_list[i].remove(shot)
                #        game_board[user_x][user_y] = 'X'

            else:
                print("THAT'S A MISS...")
                # game_board[user_x][user_y] = 'O'

    except ValueError:
        print("ERROR: You tried to input a non-numeral value, please try again.")

def are_unsunk_ships_left(fleet):
    if not any(ship_list):
        print("You destroyed all ships in the fleet!")
    else:
        print("There are ships remaining!")


# create list to hold the fleet
ship_fleet = {}
ship_list = []

# creates an empty board
game_board = []

# calls blank_board against the empty board
blank_board(10, 10)

print(ship_list)
print(ship_fleet)
show_grid(game_board)

randomly_place_ships()

show_grid(game_board)
print(ship_list)
print(ship_fleet)

check_if_hits(input("Please enter a value for row: "), input("Please enter a number for value of column: "), 'Navy')

# PROBLEM:
#   Can now remove entries, but this was by putting them in as STRINGS - NOT IDEAL
