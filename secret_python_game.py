import random
secret =random.randint(1,10)
print("===== Number Guess in a Game =====")
print("Guess a Number between 1 and 10")

while True:
    guess =int(input("Enter your guess:"))

    if guess == secret:
         print("Congratulation! You Guessed the correct number.")
         break
    elif guess < secret:
         print("Too Low! Try Again.")
else:
        print("Too High! Try Again.")

print("Game Over!")   
''''import random

secret = random.randint(1, 10)

print("===== Number Guess Game =====")
print("Guess a Number between 1 and 10")

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < secret:
        print("Too Low! Try Again.")
    else:
        print("Too High! Try Again.")

print("Game Over!")'''
