import random
player = input("What's your name?")
winChance = random.randrange(100)

if winChance >= 50:
    print("You win the game, " + player + "!")
else:
    print("You lost the game, " + player + ".")

input()
