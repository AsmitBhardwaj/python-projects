import random

#we will make a blackjack game here

"""
we are going to make a card dictionary first which will store the values of all the cars
"""

#this method will be called to deal cards
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#method to calculate score of the user or the computer
def calculate_score(cards):
    #we will add a special case for ace
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # second special case for ace where we need its value to be 1
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Computer has a blackjack!"
    elif u_score == 0:
        return "User has a blackjack!"
    elif u_score > 21:
        return "Computer won the game!"
    elif c_score > 21:
        return "User won the game!"
    elif u_score > c_score:
        return "You won the game!"
    else:
        return "Computer won the game!"

#Deal both user and computer a starting hand of 2 random card values.
user_cards = []
computer_cards = []
is_game_over = False
computer_score = -1

#method to assign cards to the user and the computer
for cards in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
while not is_game_over:
    # now we will store the score of the user and computer
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    # we will print the card scores and the computer's first card
    print(f"Your current score is {user_score} and your cards are {user_cards}")
    print(f"Computer's first card score is {computer_cards[0]}")

    # incase anyone got over 21 already its game over
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type y to get another card or type n to pass")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

#we will add more information
print(f"Your final score is {user_score} and the cards are {user_cards}")
print(f"Computer's final score is {computer_score} and the cards are {computer_cards}")

print(compare(user_score, computer_score))







