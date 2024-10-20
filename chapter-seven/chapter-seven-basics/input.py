# prompt = "\nWhat's your name? "
# Another way to solve this problem is by directly writing the prompt message inside the while loop as I did, but
# then I would have to add the name of the variable instead of the message I want to be displayed
message = ""
while message != "quit":
    # This is another way to solve this problem, I can assign an input to the message variable without pre-adding any
    # prompt text before the while loop, as the book says
    message = input("What's your name? ")
    capitalize = input("Would you like to capitalize your name? ")

    # In this portion of the code, I tried to make the code more interactable by asking the user whether they want to
    # capitalize their name or not
    if capitalize == "yes" or capitalize == "y":
        print(message.title())
    elif capitalize == "no" or capitalize == "n":
        print(message)
    # I still need to find a way to make this program work, if the user does not type any of the given answers in the
    # previous if tests, the program simply ignores whatever inputs I pass and returns to ask my name
