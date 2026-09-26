import random

print("Welcome to the number guessing game")
print("I'm thinking of a numer between 1 and 100")

number_to_guess = random.randint(1, 100)
diff_choice = input("Choose a difficulty. Type easy/hard")
attempts_left = 0

if diff_choice == "easy":
    attempts_left = 10
else:
    attempts_left = 5


while True:
    if attempts_left == 0:
        print("You've lost.")
        break
    guess = int(input("Make a guess: "))
    if guess == number_to_guess:
        print("You got it!")
        break
    diff = number_to_guess - guess
    if diff < 0:
        print("Too high. \n Guess again.")
        attempts_left -= 1
    else:
        print("Too low. \nGuess again.")
        attempts_left -= 1
