sandwich_orders = ["tuna", "pastrami", "meat", "pastrami", "cheese", "chicken", "pastrami", "vegetarian"]
finished_sandwiches = []

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print("Sorry, the deli has run out of pastrami\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Finishing {current_sandwich} sandwich")
    finished_sandwiches.append(current_sandwich)

print("\nThis is the list of sandwiches that have been finished:")
for sandwich in finished_sandwiches:
    print(sandwich)
