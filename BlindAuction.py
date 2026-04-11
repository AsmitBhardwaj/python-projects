bid_dictionary = {}

#make a boolean statement which will check if bidding is continuing
bidding_continue = True

while bidding_continue:
    name = input("What is your name? ")
    #bid will either be a float or an int
    bid = float(input("What is your bid? "))

    # ask if any more bid
    cont = input("Would you like to continue (yes/no)? ")

    if cont.lower() == "yes":
        bidding_continue = True
    elif cont.lower() == "no":
        bidding_continue = False
    else:
        print("Thank you for bidding")

    #add the bid to the main bid dictionary which we can retrieve later
    bid_dictionary[name] = bid



#initialize highest_bid and name beforehand
highest_bid = 0
winner = ""

for name in bid_dictionary:
    bid_amount = bid_dictionary[name]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = name

print(f"The winner is {winner} with the bid of {highest_bid}")
