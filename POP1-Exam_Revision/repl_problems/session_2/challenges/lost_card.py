def lost_card():
    # list to hold stored cards
    hand = []

    # n to get number of cards in hand
    n = int(input())

    # loop to get inputs and append to list
    for i in range(n-1):
        card = int(input())
        hand.append(card)

    # loop over the list and check if i is missing - i will iterate from 1 to n + 1 and check if i not in hand
    for i in range(1, n+1):
        if i not in hand:
            return i


print(lost_card())
