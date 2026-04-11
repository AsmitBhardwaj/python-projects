MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
#initializing profit
profit = 0
#total money given by user


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#make sure that we have enough ingredients for the drin
def is_ingredients_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, that requirement is not sufficient.")
            return False
    return True

#we will make a method to process coins
def process_coins():
    #returns the total value of all the coins
    print("Please insert coins: ")
    total_cost = int(input("How many quarters?: ")) * 0.25
    total_cost += int(input("How many dimes?: ")) * 0.1
    total_cost += int(input("How many nickles?: ")) * 0.05
    total_cost += int(input("How many pennys?: ")) * 0.01
    return total_cost

#we have to check if the transaction was successfull or not
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
#we have to return the change if the money is more than required cost and round it up as well
        change = round(money_received - drink_cost)
        print(f"Here is ${change} in change.")
        #make profit global variable so that it can be accessible
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry! There is not enough money. We have to cancel your order")
        return False

#we will make a method to create the coffee
def make_coffee(drink_name, order_ingredients):
    #To make the coffee we just need to subtract the required ingredients
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("Here is your coffee now.")



is_on = True

while is_on:
    # ask user for their coffee
    user_choice = input("What would you like?(espresso/latte/cappuccino)")

    #shut it down when entered off
    if user_choice == "off":
        is_on = False
    #give the ingredients when entered report
    elif user_choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[user_choice]
        print(drink)
        if is_ingredients_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])








#if we have enough resources, we ask the user for money
    #calculate the total value of money

#if the money is not enough, refund the money

#if enough money is there, add it to profit and write it when report is written

#if added more money, return the difference/change

#if enough money and change stuff done, we start making the drink and deduct the ingredients from the report

#tell the user to enjoy their drink
