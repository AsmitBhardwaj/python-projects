# first of all we will add all the 4 methods

#add method
def add(n1, n2):
    return n1 + n2

#subtract method
def subtract(n1, n2):
    return n1 - n2

#multiply method
def multiply(n1, n2):
    return n1 * n2

#divide method
def divide(n1, n2):
    return n1 / n2

""" 
we will create a dictionary where we will be storing the symbols which will do the functions
"""

sign_dictionary = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

#print(sign_dictionary["*"](4, 8))
def calculator():
    # now we will ask the user for the first number
    n1 = int(input("Enter the first number:"))

    should_continue = True

    while should_continue:
        sign = input("Enter the operation you want to perform:")
        n2 = int(input("Enter the second number:"))
        print((sign_dictionary[sign](n1, n2)))
        # we will store incase we need that later
        ans = (sign_dictionary[sign](n1, n2))

        next_step = input("Do you want to perform another operation?(yes/no): ")
        if next_step.lower() == "yes":
            n1 = ans
        elif next_step.lower() == "no":
            should_continue = False
            calculator()
        else:
            should_continue = False
            print("Thank you for using this calculator")
#my dumbass did not call the calculator
calculator()






