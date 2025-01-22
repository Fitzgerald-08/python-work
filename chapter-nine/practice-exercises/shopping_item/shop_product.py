class ShoppingItem:
    """Model interactive shopping items"""

    def __init__(self, name, amount, total_price):
        """Initialize the basic attributes for a given item from a store"""
        self.name = name
        self.amount = amount
        self.total_price = total_price

    def get_total_price(self):
        """Give users the total price for the items they decided to purchase"""
        purchase_resume = (f"Product: {self.name}\n"
                           f"Quantity: {self.amount}\n"
                           f"Total: ${self.total_price}")

        return purchase_resume


# In this part I am going to create a dictionary containing all the information for each product the store sells
# Also, I am going to store what each prompt should say and some formatting

shopping_items = {
    "shampoo": 15,
    "body soap": 10,
    "tooth paste": 12,
    "toilet paper": 8,
    "kitchen oil": 6,
    "egg": 0.5,
    "cheese bar": 5,
}

product_prompt = (f"Enter product:\n"
                  f"Hit 'q' to exit program\n")

quantity_prompt = "Enter quantity:\n"

show_product_prompt = ("Sorry, the selected product is not available\n"
                       "Would you like to see the available items?(y/n)\n")

# Now, I am going to write the main part of the program

active = True

# First, get the type of product the user wants to purchase and then make sure it exists in the inventory

product = ""
while product != "q":
    product = input(product_prompt)
    product.strip()
    product.lower()

    # This is statement will simply quit whenever the users wants to by pressing 'q'
    if product == "q":
        break
    # If they entered one available product, the program will continue
    elif product in shopping_items.keys():
        # Once I make sure the user has selected an available product, it's time to ask for the desired quantity
        quantity = int(input(quantity_prompt))

        # If it is a negative value or more than 49, it will trigger an error
        if quantity < 0 or quantity > 49:
            while True:
                print("Sorry, you can only enter positive values and it can not be more than 49")
                quantity = int(input(quantity_prompt))
        # But if they entered a correct value the program will continue it's way down all the way until performing
        # an arithmetic operation
        else:
            # Here I am going to define what the final price for this product will be
            price = quantity * shopping_items[product]

            # And finally, I will put everything into place
            shopping_item = ShoppingItem(product, quantity, price)
            print(shopping_item.get_total_price())

    # Just in case the user made a typo or selected an unavailable item
    else:
        show_product = input(show_product_prompt)

        # Display the product list if the user has entered an available product
        if show_product == "y":
            for shopping_item, price in shopping_items.items():
                print(f"-{shopping_item.title()}: {price}")
        # If they don't want to, go back to the beginning of the program
        elif show_product == "n":
            continue
        # And if they didn't select any of the possible answers, (y/n)
        else:
            true_flag = True
            while true_flag:
                show_product = input("You can only enter 'y' and 'n'(for yes and no)")

                # Only until they have selected 'y' or 'n' they will be able to continue
                if show_product == "y" or show_product == "n":
                    true_flag = False
