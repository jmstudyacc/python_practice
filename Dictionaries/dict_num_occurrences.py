"""
The text is given in a single line. For each word of the text count the number of its occurrences before it.
A word is a sequence of non-whitespace characters. 
Two consecutive words are separated by one or more spaces. (Punctuation marks are a part of a word, by this definition.)

For example, on input:
the block on the block on the block on the floor
output must be
0 0 0 1 1 1 2 2 2 3 0
"""
usr_lst = []
usr_ipt = "the block on the block on the block on the floor".split()
usr_set = set()
usr_dct = {}

#usr_ipt = input().split()
#usr_lst = []

for i in usr_ipt:
    if i not in usr_lst:
        print(0, end=" ")
        usr_lst.append(i)

    elif i in usr_lst:
        print(usr_lst.count(i), end=" ")
        usr_lst.append(i) 

"""
#print(set(usr_lst))

for i in usr_ipt:
    if i not in usr_dct:
        #print(usr_dct)
        usr_dct[i] = 0
    else:
        usr_dct[i] += 1
    print(usr_dct[i], end= " ") 

for word in words:
  if word in d:
    d[word]+=1
  else:
    d[word] = 0
  print(d[word], end = " ")  
"""
