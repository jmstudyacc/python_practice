def word_pairs():
    # initialise the dictionary
    synonyms = {}

    # specify the expected number of word pairs
    pair_count = int(input())

    # loop until you hit the expected number
    for i in range(pair_count):
        # entry into dictionary is input from user sep by space
        entry = input()

        # split the string to get a list
        entry = entry.split(" ")

        # populate the dict with key = 0 entry in list with value = 1 entry in list
        synonyms[entry[0]] = entry[1]

    # searching for a key/value pair
    search = input()

    # return result of the search
    return synonyms.get(search)


print(word_pairs())