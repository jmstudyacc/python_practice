
# Given a string in which the letter h occurs at least twice, 
# replace every occurrence of the letter h by the letter H, 
# except for the first and the last ones.

# Example Input: 'In the hole in the ground there lived a hobbit'

# Example Output: 'In the Hole in tHe ground tHere lived a hobbit'

inp = input()

h_inp = inp.count('h')
h_lfind = inp.find('h')
h_rfind = inp.rfind('h')

old_inp = inp[h_lfind+1:h_rfind]
new_inp = old_inp.replace('h', 'H')

#print(new_inp + "\n" + old_inp)

if h_inp >= 2:
	print(inp.replace(old_inp, new_inp))


# Given a string, delete all its characters whose indices are divisible by 3

# Example Input: 'Python'

# Example Output: 'yton'

words = input()

list_words = list(words)

#count_words = len(words)
#print(count_words)

looped_list = []

count = 0

for i in list_words:
	#print(count)
	if count % 3 != 0:
		looped_list.append(i)
	count += 1

strung_list = ''.join(looped_list)
print(strung_list)

