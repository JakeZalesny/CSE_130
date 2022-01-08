"""
1. Jake Zalesny
2. Guessing Game
3. This Program is meant to be a guessing game, 
it randomly generates a number which the players
will have to guess
4. The hardest part for me was remembering the syntax
that I used last year. 
5. It took me approximately 45min - 1hr
"""
import random

def get_upper_bound(): 
    upper_bound = int(input("Pick a positive integer: "))
    return upper_bound

def get_random_number(upper_bound):
    random_number = random.randint(1, upper_bound)
    return random_number

def play_guessing_game(upper_bound, random_number):
    guesses = []
    guess = 0 
    counter = 0
    print(f"Guess a number between 1 and {upper_bound}")
    while guess != random_number :
        guess = int(input("> "))
        guesses.append(guess)
        counter += 1
        if guess > random_number :
            print("Too high!")
        if guess < random_number :
            print("Too low!")
        if guess == random_number :
            print("Correct!")
            break
    return guesses, counter

upper_bound = get_upper_bound()
random_number = get_random_number(upper_bound)
guesses, counter = play_guessing_game(upper_bound, random_number)

print(f"You got it in {counter} guesses!")

print("The numbers you guessed were: ", end="")
print("[", end="")
count = 1
for line in guesses : 
    if count != len(guesses) :
        print(line, end="")
        print(", ", end="")
    
    elif count == len(guesses) :
        print(line, end="")
    count += 1

print("]", end="")
