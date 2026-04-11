#1) add logo of the game
from art import logo, vs
#import the celebrity data from game_data
from game_data import data
import random

#3) format data into printable form
#we will make this into a method
def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_description} from {account_country}.")

#method to check if the answer is correct
def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        """
        if user_guess == "a":
            return True
        else:
            return False"""
        #we will shorten this
        return user_guess == "a"
    else:
        return user_guess == "b"
#because account b will become account a after guessing correctly
account_b = random.choice(data)

print(logo)
game_should_continue = True
while game_should_continue:
    # 2)assign value to a and b where the celebrities will be posted
    account_a = account_b
    account_b = random.choice(data)

    # keep track of the score
    score = 0

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare a: {format_data(account_a)}")
    print(vs)
    print(f"Compare b: {format_data(account_b)}")

    # 4) ask the user for a guess
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #clear the screen
    print("\n" * 20)
    print(logo)

    # 5) check if the user guess is correct
    # get follower count of both accounts
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    # check if user is correct
    is_correct = check_answer(user_guess, a_followers, b_followers)

    # 6)give user feedback on their guess
    if is_correct:
        score += 1
        print(f"Congratulations, you guessed it right! Score : {score}")
    else:
        print(f"Sorry, that's wrong. Final score is {score}")
        game_should_continue = False

#7) keep track of user score

#8) repeat the game
#9) make account B into account A