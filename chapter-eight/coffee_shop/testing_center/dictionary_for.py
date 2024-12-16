# I can use a for loop with dictionaries in which there is one (or more) key-value
# pair consists of a string and an integer

coffee = {
    "cappuccino": 5,
    "chai": 3.55,
    "frappe": 6,
    "espresso": 4,
}

for coffee, price in coffee.items():
    full_description = f"{coffee.title()}: ${price}"
    print(full_description)
