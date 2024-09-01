pizzas = ["Pepperoni", "Cheese", "Vegetarian"]
friends_pizza = pizzas[:]

pizzas.append("Duck")
friends_pizza.append("Chicken")

for pizza in pizzas:
    print(f"{pizza} is one of my favorite flavours of pizzas")

for new_pizza in friends_pizza:
    print(f"{new_pizza} is one of my friend's favorite flavours of pizza")

print("\nI really, really love pizza")
