letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
points = [
    1,
    3,
    3,
    2,
    1,
    4,
    2,
    4,
    1,
    8,
    5,
    1,
    3,
    4,
    1,
    3,
    10,
    1,
    1,
    1,
    1,
    4,
    4,
    8,
    4,
    10,
]

letter_to_points = {
    k: v for k, v in zip(letters, points)
}  # Taking the 2 separate lists and joining them into a single list

letter_to_points[" "] = 0  # Adding in a value for " "


def score_word(word):  # Defining a function to collect points of words
    word = word.upper()  # Change the word to uppercase to match the dictionary
    point_total = 0  # initialise word point_totals

    for i in word:  # iterate over each character in word
        # point_total counter adds the value associated with the letter represented by 'i' - using .get() here with a default value
        point_total += letter_to_points.get(i, 0)

    return point_total  # return the point_total


print(score_word("brownie"))

player_to_words = {
    # Creating a dictionary with a list as value
    "player1": ["blue", "tennis", "exit"],
    "wordNerd": ["earth", "eyes", "machine"],
    "Lexi Con": ["eraser", "belly", "husky"],
    "Prof Reader": ["zap", "coma", "period"],
}

player_to_points = {}

# Key is referred to as 'player' and value is referred to as 'words'
for (player, words,) in (player_to_words.items()):
    player_points = 0  # player_points counter

    for word in words:  # first loop iterates over each combination of key:value
        # player_points adds the returned score of the word, calling previous function
        player_points += score_word(word)

    # assign the player name and their point score to the empty dictionary
    player_to_points[player] = player_points


def winner_player(d):
    v = list(d.values())
    k = list(d.keys())

    return k[v.index(max(v))]


winner = winner_player(player_to_points)

print(f"The winner is: {winner} with {player_to_points.get(winner)} points")
