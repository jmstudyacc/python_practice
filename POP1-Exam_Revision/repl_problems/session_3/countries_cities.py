def get_key(dict1, val):
    # the dictionary and desired value is passed to the function
    for key, value in dict1.items():
        # iterate over dict1.items() - which is a list looking at key and value
        for k in value:
            # new loop to check the values WITHIN the list value
            if k == val:
                # if k matches the desired val then that key is target key...
                return len(dict1.get(key))      # return the LENGTH of the value associated with the key

    return "key doesn't exist"


def countries_cities():
    # initialise the dictionary
    locations = {}
    count = int(input())

    for i in range(count):
        entry = input().title().split(" ")
        if entry[0] in locations:
            locations[entry[0]].append(entry[1])
        else:
            locations[entry[0]] = [entry[1]]

    city = input().title()
    return get_key(locations, city)


print(countries_cities())


"""
4
uk london
uk leeds
fr paris
de berline
leeds
"""