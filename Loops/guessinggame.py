# Guessing game
# generate a random integer between 1 to 100

import random
jackpot = random.randint(1, 100)

guess = int(input("Guess number: "))
counter = 1
while guess != jackpot:
 if guess < jackpot:
   print("Righit ! Guess Higher")
 else:
   print("Wrong ! Guess Lower")
 

guess = int(input("Guess number: "))
counter += 1


print("Correct Guess")
print("Attempts", counter)