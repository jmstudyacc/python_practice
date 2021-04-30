# Enter your code here. Read input from STDIN. Print output to STDOUT

def word_order():
    num_words = int(input())
    # create a dictionary to store the words
    words = {}

    # loop for the value input by user
    for _ in range(num_words):
        # get word input from user
        word = input()
        # if the word is not in the dictionary (fast in Python)
        if word not in words:
            # add a new entry to the dictionary with 1 as count
            words[word] = 1
        else:
            # if it is already present increment the value by 1
            words[word] += 1

    # print the size of the dictionary by getting length
    print(len(words))
    # iterate over dictionary and print each numerical value associated with the key (i)
    for i in words:
        print(words[i], end=" ")


word_order()
