w = "Rock"
x = "Paper"
y = "Scissors"
z = input("Rock, Paper, Scissors, Shoot!: ")
import random
randint = random.choice(w, x, y)
elif z == randint :
    print("Tie. Try again.")
    print(randint)
elif randint == w and z == x :
    print("You Win!")
    print(randint)
elif randint == x and z == y :
    print("You Win!")
    print(randint)
elif randint == y and z == w :
    print("You Win!")
    print(randint)
elif randint == w and z == y :
    print("You Lose.")
    print(randint)
elif randint == x and z == w :
    print("You Lose.")
    print(randint)
elif randint == y and z == x :
    print("You Lose.")
    print(randint)
