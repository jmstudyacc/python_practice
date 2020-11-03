"""
First line of the input is a number, which indicates how many pairs of words will follow (each pair in a separate line). 
The pairs are of the form COUNTRY CITY specifying in which country a city is located. 
The last line is the name of a city. Print the number of cities that are located in the same country as this city.

Hint. Use dictionaries. 

For example, on input:
6

UK London
US Boston
UK Manchester
UK Leeds
US Dallas
Russia Moscow

Manchester

Output must be:
3

"""
loc_dict = {}
loc_list = []
num_entries = int(input())

for i in range(0, num_entries):
    user_entry = input().split()         # Splits the input by " " and makes it a list
    loc_list.append(user_entry)          # Append the item to a list

for key, value in loc_list:             # iterate over the list with 2 identifiers, key & value
    if key not in loc_dict:             # if the key does not exist in the dictionary
        loc_dict[key] = []              # add it with an empty value
    loc_dict[key].append(value)         # for the 'key' in the list currently being iterated e.g. UK, append the value found in the list e.g. London

city_lookup = input()                   # request input from user for the target city

for key, value in loc_dict.items():     # for key, value pair in the dictionary
    if city_lookup in value:            # if the user input for city matches the value
        count = len(value)              # count is assigned to the length of the values of that key
        print(count)


"""
N = int(input())

d = {}

for i in range(0,N):
  pair = input().split()
  if pair[0] in d:
    d[pair[0]].append(pair[1])
  else:
    d[pair[0]] = [pair[1]]

city = input()

for country, cities in d.items():
  if city in cities:
    print(len(d[country]))
"""