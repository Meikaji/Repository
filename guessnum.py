z = input("Guess the Number: ")
import random
randnum = random.randrange(1,9)
print (z)
print (randnum)
if z == randnum :
    print("You Win.")
else :
    print ("You lose.")