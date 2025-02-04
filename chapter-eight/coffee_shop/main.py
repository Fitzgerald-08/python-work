from identification import identify_guest
from order_process import arrange_values

# Here I am defining each message for the user to know what to prompt
# I decided to do it this way because I consider it's easier to change something if I wanted to
welcome_prompt = "Hello and welcome to Networkchuck's coffee shop\n"
order_prompt = "What would you like to order?\n"
order_prompt += "('q' to quit program, 'menu' to display menu)\n"
quantity_prompt = "How many would you like to order?\n"
size_prompt = "Choose a size for your coffee (s/m/l)\n"

coffee_menu = {
    "cappuccino": 5,
    "chai": 3.50,
    "espresso": 4,
    "ristretto": 5.50,
    "frappe": 6,
    "latte": 5,
    "flat white": 4.50,
    "macchiato": 6,
    "moka": 5,
}

# This is where I'll (hopefully) store individual values for both each coffee ordered and...
# its price, then I'll put it all together in a dictionary which will make out the final order
coffee_ordered = []
coffee_price = []
coffee_size = []

# This is where I will store the values relevant to calculate the final price of the order
final_order = {

}

# Here's the part where the program actually starts
print(welcome_prompt)

# In order to pass a value to the function and directly enter the while loop,
# I have to use an empty string, just like in repeat_question.py file
name = ""
guest_approved = identify_guest(name)

print(f"Hello {guest_approved.title()}, it is a pleasure to have you here\n")

# Here's where I am going to make the main part of the program, which processes the information
# First, I am going to take the user's order
order = ""
while order != "q":
    order = input(order_prompt)
    order.lower()
    order.strip()

    # I decided to use the 'in' keyword to check whether the coffee they entered exists
    if order in coffee_menu:
        print(f"Adding {order.title()}...")
        coffee_ordered.append(order)

        # Now, I am going to ask the user how many pieces of coffee they would like to order
        quantity = ""
        while quantity != "q":
            quantity = int(input(quantity_prompt))

            if quantity == "q":
                quantity = str
                break
            elif quantity == 1:
                print("Adding 1 coffee...")
                coffee_order = quantity * coffee_menu[order]
                coffee_price.append(coffee_order)

                # Finally, let the user choose a size for his coffees
                size = ""
                while size != "q":
                    size = input(size_prompt)
                    size.lower()
                    size.strip()

                    if size == "s":
                        print("Adding a small coffee...")
                        coffee_size.append("small")
                        break
                    elif size == "m":
                        print("Adding a medium coffee...")
                        coffee_size.append("medium")
                        break
                    elif size == "l":
                        print(f"Adding a large coffee...")
                        coffee_size.append("large")
                        break
                    else:
                        print("Sorry, you can only order small, medium or large coffees")

                break
            elif 2 <= quantity <= 29:
                print(f"Adding {quantity} coffees...")
                coffee_order = quantity * coffee_menu[order]
                coffee_price.append(coffee_order)

                # For now, I'll add the same block of code to handle coffee sizes
                size = ""
                while size != "q":
                    size = input(size_prompt)

                    if size == "s":
                        print("Adding a small coffee...")
                        coffee_size.append("small")
                        break
                    elif size == "m":
                        print("Adding a medium coffee...")
                        coffee_size.append("medium")
                        break
                    elif size == "l":
                        print("Adding a large coffee...")
                        coffee_size.append("large")
                        break
                    else:
                        print("Sorry, you can only order small, medium or large coffees")

                break
            else:
                print("Sorry, the number you entered is invalid\n"
                      "(You can only order from 1 through 29")

    elif order == "q":
        break
    # Let the user know what's on the menu
    elif order == "menu":
        for coffee, price in coffee_menu.items():
            coffee_info = f"{coffee.title()}: ${price}"
            print(coffee_info)

    # If it doesn't, then I am going to display the following message
    else:
        print(f"Sorry, we do not serve {order.title()}, or there's a typo in your order")


arrange_values(coffee_ordered, coffee_size, coffee_price)
# Print results in order to make sure everything works fine... for now
for coffee in coffee_ordered:
    print(coffee.title())

for price in coffee_price:
    print(price)

for size in coffee_size:
    print(size.title())
