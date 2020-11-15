import time
import random

i = True
#money = 100
#print(random.randint(1,2))

#Write your game of chance functions here
def coin_flip():
    money = 100
    while i == True:
        print("\nYou are about to flip your coin!")
        time.sleep(0.25)
        bet = input("You have "+str(money)+" gold coins, would you like to bet on this game?\nPlease type, Yes or No: ")
        bet = bet.lower()
        time.sleep(0.25)
        if bet == 'yes' or bet == 'y' and money > 0:
           coins = int(input("How many gold coins would you like to bet?: "))
           if coins >= 25 and coins < 50:
               print("Hey there big spender!")
               time.sleep(0.75)
           elif coins >= 50:
               print("Wooooooooooah!! Don't go gambling away your rent money!")
               time.sleep(0.75)
           else:
               print("Sorry buddy but no betting for you!")
               time.sleep(0.75)
        else:
          coins = 0
               
        coin_call = (input("What option will you pick - Heads or Tails?: "))
        coin_call = coin_call.lower()
        if coin_call == "heads" or coin_call == "tails" or coin_call == "h" or coin_call == "t":
            print("3...2...1...Flip!")
            time.sleep(1)
            print("*Flipping Coin Noises...*")
            time.sleep(1)
            print("The result is...")
            time.sleep(1.0)
            coin_toss = random.randint(1,2)
            if coin_toss == 1:
                print("\nTails!")
                if coin_toss == 1 and coin_call == 'tails' or coin_call == 't':
                  time.sleep(0.5)
                  print("\nYou are a winner! You won "+str(coins))
                  money += coins
                  time.sleep(0.5)
                  print("Your new total of gold coins is "+str(money))
                  time.sleep(1)
                else:
                  time.sleep(0.5)
                  print("\nBetter luck next time! You lost "+str(coins))
                  money -= coins
                  time.sleep(0.5)
                  print("Your new total of gold coins is "+str(money))
                  time.sleep(1)
            else:
                print("\nHeads!")
                if coin_toss == 2 and coin_call == "heads" or coin_call == "h":
                    time.sleep(0.5)
                    print("\nYou are a winner! You won "+str(coins))
                    money += coins
                    time.sleep(0.5)
                    print("Your new total of gold coins is "+str(money))
                    time.sleep(1)
                else:
                    time.sleep(0.5)
                    print("\nBetter luck next time! You lost "+str(coins))
                    money -= coins
                    time.sleep(0.5)
                    print("Your new total of gold coins is "+str(money))
                    time.sleep(1)
        else:
            print("\nPlease select Heads or Tails.")
            time.sleep(1.5)
    
#Call your game of chance functions here

choice = int(input("Which game would you like to play?\n\n 1 - A game of Coin Toss.\n 2 - A game of Cho-Han.\n\n"))
if choice == 1:
   coin_flip()
elif choice == 2:
   cho_han()
