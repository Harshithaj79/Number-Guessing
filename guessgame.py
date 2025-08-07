'''It is a game program
that is mainly to guess a number between 1 to 100
if it matches with the computer then you won'''
import random
print('The game is to guess a number between 1 to 100.If youu match with the computer then you won')
a =random.randint(1, 100)
b = int(input("Enter your number between 1 to 100:"))
while a!=b:
    print("You guessed wrong number, try again")
    print("Hint is : ",end="")
    if (a>b):
            print("The number is greater than your guess")
    elif (a<b):
            print("The number is less than your guess")
    b = int(input())
if a==b:
     print("You cracked the computer mind🫡.\n Congrats 🤝YOU WON!🥳🥳")