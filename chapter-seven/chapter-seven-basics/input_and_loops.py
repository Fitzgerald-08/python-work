# In the following three lines of code, I am defining the message to be displayed to the user with clear instructions
prompt = "\nWhat toppings would you like to put in your pizza?"
prompt += "\nIf the topping you have chosen is not available we'll let you know"
prompt += "\nType 'menu' to see the list of available toppings"
prompt += "\nPlease, enter toppings of your choice: "

# Here, I have created the list of toppings the user can choose from
toppings = ["pepperoni", "salami", "pineapple", "sausage", "red pepper", "pesto", "spinach", "black olives",
            "red onion", "shrimp", "scallops", "mushrooms", "extra cheese", "bacon", "onions", "chicken"]

# This empty list wil be useful right at the end of the program, as it will let me display the full list of chosen
# toppings
selected_toppings = []

# I have already explained this, but I'll do it again. Basically, what this does is the "message" is evaluated by the
# while loop, and once inside, it prompts the user for a topping of choice, if it is not available, it will break out
# of the while loop,if it is available, it will save the topping inside the empty list previously created
message = ""
while message != "quit":
    message = input(prompt).lower()
    if message == "quit":
        break
    elif message == "menu":
        for topping in toppings:
            print(f"-{topping.title()}")
    else:
        if message in toppings:
            print(f"Got it, we'll add <{message}> to your pizza")
            selected_toppings.append(message)
        else:
            print(f"Sorry, we do not have <{message}> in our list of available toppings, but we have the following:")
            print(f"{toppings}")
            continue

print(f"\nThis is the list of toppings you have selected:")
for topping in set(selected_toppings):
    print(f"-{topping.title()}")

removing_topping = input("\nWould you like to make any changes to your pizza? ")
if removing_topping == "yes":
    prompt = "Which topping would you like to remove? "
    removedTopping = ""
    while removedTopping != "quit":
        removedTopping = input(f"\n{prompt}")
        if removedTopping in selected_toppings:
            selected_toppings.remove(removedTopping)
        elif removedTopping == "quit":
            break
        else:
            print(f"<{removedTopping.title()}> is not in the list, this is the list of toppings you have selected:")
            for topping in selected_toppings:
                print(f"-{topping.title()}")
else:
    exit()

print(f"\nPerfect, your pizza with the following toppings will be ready shortly")
for topping in selected_toppings:
    print(f"-{topping.title()}")
