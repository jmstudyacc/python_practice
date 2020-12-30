from random import randint, choice


def blank_board(m, n):
    # header_row = [[' ', '|', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['-'] * 13]
    # game_board.extend(header_row)
    for z in range(m):
        # row = [str(z)] + ['|'] + ['.'] * n
        row = ['.'] * n
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


def check_if_hits(row, column, fleet):
    # row & column are used to construct the tuple
    # fleet is then used to determine the construct to iterate over

    def show_grid(board):
        # this is not efficient - how to keep the last grid and only change the new changes?
        print("\n" + "*" * 20)

        # \u0332 underlines the string that joins
        print('{:s}'.format('\u0332'.join("\nThe updated board: \n")))

        # prints the board out
        [print(" ".join(game_board[i])) for i in range(len(game_board))]


def hit(row, column, fleet):
    pass
    # returns a tuple (fleet1, ship)


def is_open_sea(row, column, fleet):
    # row & column used to build the tuple
    # fleet used for the iterator - iterate over the list? dictionary?
    if one_coord_whitespace_check(row, column, fleet):
        return True
    else:
        return False


def is_sunk(ship):
    pass


def are_unsunk_ships_left(fleet):
    pass


def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    pass


def one_coord_whitespace_check(x, y, fleet):
    fleet_set = fleet
    if (x - 1, y - 1) not in fleet_set and \
            (x - 1, y) not in fleet_set and \
            (x - 1, y + 1) not in fleet_set and \
            (x, y - 1) not in fleet_set and \
            (x, y + 1) not in fleet_set and \
            (x + 1, y - 1) not in fleet_set and \
            (x + 1, y) not in fleet_set and \
            (x + 1, y + 1) not in fleet_set:
        return True
    else:
        return False


def start_coord_horizontal_whitespace_check(x, y, fleet):
    # function to check the start coord (leftmost) of a horizontal ship that forms to the right
    fleet_set = fleet
    if (x - 1, y - 1) not in fleet_set and \
            (x - 1, y) not in fleet_set and \
            (x - 1, y + 1) not in fleet_set and \
            (x, y - 1) not in fleet_set and \
            (x, y + 1) not in fleet_set and \
            (x + 1, y - 1) not in fleet_set and \
            (x + 1, y + 1) not in fleet_set:
        return True

    else:
        return False


def internal_coord_horizontal_whitespace_check(x, y, fleet):
    fleet_set = fleet
    # function to check any internal coord (middle coord(s)) of a horizontal ship that forms to the right
    if (x, y - 1) not in fleet_set and \
            (x, y + 1) not in fleet_set:
        return True
    else:
        return False


def end_coord_horizontal_whitespace_check(x, y, fleet):
    fleet_set = fleet
    # function to check the end coord (rightmost) of a horizontal ship that forms to the right
    if (x, y - 1) not in fleet_set and \
            (x, y + 1) not in fleet_set and \
            (x + 1, y - 1) not in fleet_set and \
            (x + 1, y) not in fleet_set and \
            (x + 1, y + 1) not in fleet_set:
        return True
    else:
        return False


def start_coord_vertical_whitespace_check(x, y, fleet):
    fleet_set = fleet
    # function to check the start coord (topmost) of a vertical ship that forms downwards
    if (x - 1, y - 1) not in fleet_set and \
            (x - 1, y) not in fleet_set and \
            (x, y - 1) not in fleet_set and \
            (x + 1, y - 1) not in fleet_set and \
            (x + 1, y) not in fleet_set:
        return True
    else:
        return False


def internal_coord_vertical_whitespace_check(x, y, fleet):
    fleet_set = fleet
    # function to check any internal coord (middle coord(s)) of a vertical ship that forms downwards
    if (x - 1, y) not in fleet_set and \
            (x + 1, y) not in fleet_set:
        return True
    else:
        return False


def end_coord_vertical_whitespace_check(x, y, fleet):
    fleet_set = fleet
    # function to check the end coord (bottommost) of a vertical ship that forms downwards
    if (x - 1, y) not in fleet_set and \
            (x - 1, y + 1) not in fleet_set and \
            (x, y + 1) not in fleet_set and \
            (x + 1, y) not in fleet_set and \
            (x + 1, y + 1) not in fleet_set:
        return True
    else:
        return False
    # if 2nd condition check passes


def ship_type(ship):
    # ship construct defines length by index 3, query this to find the length
    ship_length = list(fleet_dict.get(ship))
    ship_length = ship_length[2]

    # if statements matching the brief provided for ship lengths
    if ship_length == 1:
        return 'submarine'
    elif ship_length == 2:
        return 'cruiser'
    elif ship_length == 3:
        return 'destroyer'
    else:
        return 'battleship'


def submarine_place():
    while True:
        x = randint(0, 9)
        y = randint(0, 9)
        SUB_LENGTH = 1
        HORIZONTAL = True
        hits = {()}
        coord1 = (x, y)

        # 1st condition check to check if proposed coord is not already in fleet
        if coord1 not in fleet_set:
            # 2nd condition check for whitespace around sub
            if one_coord_whitespace_check(x, y, fleet_set):
                # if above condition is TRUE
                fleet_set.add(coord1)
                game_board[x][y] = 'S'
                return [coord1], HORIZONTAL, SUB_LENGTH, hits
            # if 2nd condition check fails
            else:
                continue

        # if 1st condition check fails
        else:
            continue


def destroyer_place():
    while True:
        x = randint(0, 8)
        y = randint(0, 8)
        horizontal = choice([True, False])
        DES_LENGTH = 2
        hits = {()}

        coord1 = (x, y)

        if horizontal:
            x_2 = x + 1
            coord2 = (x_2, y)

            # 1st condition check to confirm coords not already present in fleet & for horizontal destroyers
            if coord1 not in fleet_set and coord2 not in fleet_set and horizontal:

                # 2nd condition check to confirm whitespace for horizontal destroyer
                if (start_coord_horizontal_whitespace_check(x, y, fleet_set) and
                        end_coord_horizontal_whitespace_check(x_2, y, fleet_set)):
                    # if above condition is TRUE
                    fleet_set.add(coord1), fleet_set.add(coord2)
                    game_board[x][y] = "D"
                    game_board[x_2][y] = "D"
                    return [coord1, coord2], horizontal, DES_LENGTH, hits

                # if 2nd condition check fails
                else:
                    continue
        else:
            y_2 = y + 1
            coord2 = (x, y_2)
            # VERTICAL SHIP PLACEMENT
            if coord1 not in fleet_set and coord2 not in fleet_set and not horizontal:
                # 2nd condition check to confirm whitespace for vertical destroyer
                if start_coord_vertical_whitespace_check(x, y, fleet_set) and \
                        end_coord_vertical_whitespace_check(x, y_2, fleet_set):
                    # if above condition is TRUE
                    fleet_set.add(coord1), fleet_set.add(coord2)
                    game_board[x][y] = "D"
                    game_board[x][y_2] = "D"
                    return [coord1, coord2], horizontal, DES_LENGTH, hits
                # if 2nd condition check fails
                else:
                    continue
            # if 1st condition check fails
            else:
                continue


def cruiser_place():
    while True:
        x = randint(0, 7)
        y = randint(0, 7)
        horizontal = choice([True, False])
        CRU_LENGTH = 3
        hits = {()}

        coord1 = (x, y)

        if horizontal:
            x_2 = x + 1
            x_3 = x + 2
            coord2 = (x_2, y)
            coord3 = (x_3, y)

            if coord1 not in fleet_set and \
                    coord2 not in fleet_set and \
                    coord3 not in fleet_set and horizontal:
                if start_coord_horizontal_whitespace_check(x, y, fleet_set) and \
                        internal_coord_horizontal_whitespace_check(x_2, y, fleet_set) and \
                        end_coord_horizontal_whitespace_check(x_3, y, fleet_set):
                    # if above condition is TRUE
                    fleet_set.add(coord1), fleet_set.add(coord2), fleet_set.add(coord3)
                    game_board[x][y] = "C"
                    game_board[x_2][y] = "C"
                    game_board[x_3][y] = "C"
                    return [coord1, coord2, coord3], horizontal, CRU_LENGTH, hits
                else:
                    continue
            else:
                continue

        else:
            y_2 = y + 1
            y_3 = y + 2
            coord2 = (x, y_2)
            coord3 = (x, y_3)

            if coord1 not in fleet_set and \
                    coord2 not in fleet_set and \
                    coord3 not in fleet_set and not horizontal:
                if start_coord_vertical_whitespace_check(x, y, fleet_set) and \
                        internal_coord_vertical_whitespace_check(x, y_2, fleet_set) and \
                        end_coord_vertical_whitespace_check(x, y_3, fleet_set):
                    # if above condition is TRUE
                    fleet_set.add(coord1), fleet_set.add(coord2), fleet_set.add(coord3)
                    game_board[x][y] = "C"
                    game_board[x][y_2] = "C"
                    game_board[x][y_3] = "C"
                    return [coord1, coord2, coord3], horizontal, CRU_LENGTH, hits
                else:
                    continue
            else:
                continue


def battleship_place():
    while True:
        x = randint(0, 6)
        y = randint(0, 6)
        horizontal = choice([True, False])
        BSH_LENGTH = 4
        hits = {()}

        coord1 = (x, y)

        if horizontal:
            x_2 = x + 1
            x_3 = x + 2
            x_4 = x + 3

            coord2 = (x_2, y)
            coord3 = (x_3, y)
            coord4 = (x_4, y)

            if coord1 not in fleet_set and \
                    coord2 not in fleet_set and \
                    coord3 not in fleet_set and \
                    coord4 not in fleet_set:
                if start_coord_horizontal_whitespace_check(x, y, fleet_set) and \
                        internal_coord_horizontal_whitespace_check(x_2, y, fleet_set) and \
                        internal_coord_horizontal_whitespace_check(x_3, y, fleet_set) and \
                        end_coord_horizontal_whitespace_check(x_4, y, fleet_set):
                    # if above condition is TRUE
                    fleet_set.add(coord1), fleet_set.add(coord2), fleet_set.add(coord3), fleet_set.add(coord4)
                    game_board[x][y] = "B"
                    game_board[x_2][y] = "B"
                    game_board[x_3][y] = "B"
                    game_board[x_4][y] = "B"
                    return [coord1, coord2, coord3, coord4], horizontal, BSH_LENGTH, hits
                else:
                    continue
            else:
                continue

        else:
            y_2 = y + 1
            y_3 = y + 2
            y_4 = y + 3

            coord2 = (x, y_2)
            coord3 = (x, y_3)
            coord4 = (x, y_4)

            if coord1 not in fleet_set and \
                    coord2 not in fleet_set and \
                    coord3 not in fleet_set and \
                    coord4 not in fleet_set:
                if start_coord_vertical_whitespace_check(x, y, fleet_set) and \
                        internal_coord_vertical_whitespace_check(x, y_2, fleet_set) and \
                        internal_coord_vertical_whitespace_check(x, y_3, fleet_set) and \
                        end_coord_vertical_whitespace_check(x, y_4, fleet_set):
                    # if above condition is TRUE
                    fleet_set.add(coord1), fleet_set.add(coord2), fleet_set.add(coord3), fleet_set.add(coord4)
                    game_board[x][y] = "B"
                    game_board[x][y_2] = "B"
                    game_board[x][y_3] = "B"
                    game_board[x][y_4] = "B"
                    return [coord1, coord2, coord3, coord4], horizontal, BSH_LENGTH, hits

                else:
                    continue
            else:
                continue


def place_ship_at(row, column, horizontal, length, fleet):
    # does not return the fleet list
    ship_count = len(list(fleet_dict)) + 1
    if length == 1:
        fleet_set.add((row, column))
        fleet_dict['ship' + str(ship_count)] = [(row, column)], horizontal, length, {()}

    elif length == 2:
        if horizontal:
            fleet_set.add(((row, column), (row + 1, column)))
            fleet_dict['ship' + str(ship_count)] = [(row, column), (row + 1, column)], horizontal, length, {()}
        else:
            fleet_set.add(((row, column), (row, column + 1)))
            fleet_dict['ship' + str(ship_count)] = [(row, column,), (row, column+1)], horizontal, length, {()}

    elif length == 3:
        if horizontal:
            fleet_set.add(((row, column), (row + 1, column), (row + 2, column)))
            fleet_dict['ship' + str(ship_count)] = [(row, column), (row + 1, column), (row + 2, column)], horizontal, length, {()}

        else:
            fleet_set.add(((row, column), (row, column + 1), (row, column + 2)))
            fleet_dict['ship' + str(ship_count)] = [(row, column,), (row, column + 1), (row, column + 2)], horizontal, length, {()}

    # length is 4
    else:
        if horizontal:
            fleet_set.add(((row, column), (row + 1, column), (row + 2, column), (row + 3, column)))
            fleet_dict['ship' + str(ship_count)] = [(row, column), (row + 1, column), (row + 2, column), (row + 3, column)], horizontal, length, {()}

        else:
            fleet_set.add(((row, column), (row, column + 1), (row, column + 2), (row, column + 3)))
            fleet_dict['ship' + str(ship_count)] = [(row, column,), (row, column+1), (row, column + 2), (row, column + 3)], horizontal, length, {()}

    return list(fleet_dict)

def randomly_place_ships():
    fleet_dict['ship1'] = battleship_place()

    for cruiser in range(2, 4):
        fleet_dict['ship' + str(cruiser)] = cruiser_place()

    for destroyer in range(4, 7):
        fleet_dict['ship' + str(destroyer)] = destroyer_place()

    for submarine in range(7, 10):
        fleet_dict['ship' + str(submarine)] = submarine_place()

    fleet_dict['ship10'] = submarine_place()

    return list(fleet_dict)


game_board = []
fleet = []
fleet_dict = {}
fleet_set = set()

# place_ship_at(input("Please enter a value for row: "),
# input("Please enter a number for value of column: "))


# variable is assigned to the result of that output
print("\n0 - PRINTS A BLANK GAMEBOARD")
blank_board(10, 10)
print("\n1 - PRINT CURRENT FLEET DICTIONARY")
print(fleet_dict)
print("\n2 - PRINT CURRENT FLEET")
print(fleet, " is the current fleet.")
print("\n3 - RANDOMLY PLACE SHIPS")
fleet = randomly_place_ships()
print("SHIPS PLACED")
print("\n4 - PRINTS COORDS")
print(fleet_set, "\n")

fl_co = list(fleet_dict.values())
for i in range(len(fl_co)):
    print(fl_co[i][0])
# fleet_coords includes the coords of ships
print("\n5 - PRINTS FLEET DICTIONARY")
# fleet dict will include the horizontal as well
print(fleet_dict)
print("\n6 - PRINTS LIST OF END STATE FLEET DICTIONARY")
print(fleet)
print("\n7 - PRINTS A LIST VERSION OF THE SET FLEET_SET")
print(list(fleet_set))
print("\n8 - PRINTS A FULL GAMEBOARD")
show_grid(game_board)
print("\n9 - REQUEST A SHIP TYPE CHECK")
#print(ship_type(input("Which ship do you want to check? ")))
print("\10 - CHECK IF COORD IS OPEN SEA")
print(is_open_sea(8, 3, fleet_set))
print("11 - PLACE A SHIP IN FLEET")
loc_str = input("Enter row, column, True or False, length (1-4) to shoot (separated by space): ").split()
place_row = int(loc_str[0])
place_column = int(loc_str[1])
place_horizontal = bool(loc_str[2])
place_length = int(loc_str[3])
place_ship_at(place_row, place_column, place_horizontal, place_length, fleet_set)
loc_str = input("Enter row, column, True or False, length (1-4) to shoot (separated by space): ").split()
place_row = int(loc_str[0])
place_column = int(loc_str[1])
place_horizontal = bool(loc_str[2])
place_length = int(loc_str[3])
place_ship_at(place_row, place_column, place_horizontal, place_length, fleet_set)
print(fleet_dict)
print(list(fleet_dict))

# hit attempts are stored in set?

# place the ship and then return the values and store in the list?
# for i in range(0,4):
#   fleet.append()

# list comprehension search over dictionary values
# [key for key, val in d.items() if (5, 0) in val]

# getting the ship_type while maintaining the method from before
# print(list(d.get('ship1')))
# sget = list(d.get('ship1'))
# print(sget)

# ls = list(dict.values())
# for i in range(len(ls)):
#     print(ls[i][0])

# list of possibilities for a single coord check
# (ax-1, ay-1), (ax-1, ay), (ax+1, ay+1), (ax, ay-1), (ax, ay+1), (ax+1, ay-1), (ax+1, ay), (ax+1, ay+1)
