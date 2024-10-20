sandwich_orders = ["tuna", "meat", "cheese", "chicken", "vegetarian"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Finishing {current_sandwich} sandwich")
    finished_sandwiches.append(current_sandwich)

print("\nThis is the list of sandwiches that have been finished:")
for sandwich in finished_sandwiches:
    print(sandwich)
