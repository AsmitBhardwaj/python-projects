import random

#first ask the user for quesiton and all the formalities question

print("Hi! We are playing the number guessing game")
print("I want you to think of a number between 1 and 100 that I am thinking of")
print("I want you to guess and I will tell you if it is too less or too low")

#randomly select a number
num = random.randint(1, 100)

#keep track of number of guesses
number_of_guesses = 0
#boolean
number_guessed = False




while not number_guessed:
    guess = int(input("Guess a number between 1 and 100: "))
    number_of_guesses += 1

    # compare the guess with number now
    if guess < num:
        print("Too low")

    elif guess > num:
        print("Too high")

    else:
        print(f"Bingo!! The number is {num} and you took {number_of_guesses} guesses")
        number_guessed = True

