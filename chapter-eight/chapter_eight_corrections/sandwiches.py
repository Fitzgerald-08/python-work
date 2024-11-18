def make_sandwich(ingredients):
    """Returns a list of selected ingredients for the sandwich."""
    return ingredients


def modify_ingredients(value, ingredient_list):
    """Modify ingredients by adding or removing them based on user input."""
    if value.lower().startswith("y"):
        action = input("What would you like to do? ('r' to remove, 'a' to add): ").lower()

        if action == 'r':
            while True:
                ingredient_to_remove = input("Select ingredient to remove: ").strip()
                if ingredient_to_remove == "q":
                    break
                if ingredient_to_remove in ingredient_list:
                    ingredient_list.remove(ingredient_to_remove)
                    print(f"Removed {ingredient_to_remove}.")
                else:
                    print("Sorry, ingredient not found.")
        elif action == 'a':
            while True:
                new_ingredient = input("Enter new ingredient (or 'q' to quit): ").strip()
                if new_ingredient == "q":
                    break
                if new_ingredient:
                    ingredient_list.append(new_ingredient)
        else:
            print("Invalid option. Please choose 'r' or 'a'.")
    return ingredient_list


def ask_yes_no(prompt):
    """Helper function to ask yes/no questions."""
    response = input(prompt).strip().lower()
    if response.startswith("y"):
        return True
    elif response.startswith("n"):
        return False
    return ask_yes_no(prompt)  # Ask again until valid answer


# Main program loop
ingredient_list = []
while True:
    ingredient = input("Enter desired ingredients (or 'q' to finish): ").strip()
    if ingredient == 'q':
        break
    if ingredient:
        ingredient_list.append(ingredient)

print("\nIngredients selected:")
for ingredient in ingredient_list:
    print(f"- {ingredient}")

if ask_yes_no("\nWould you like to modify your selection? (yes/no): "):
    ingredient_list = modify_ingredients(input("Would you like to modify the sandwich? (y/n): "), ingredient_list)

print("\nFinal list of ingredients:")
for ingredient in ingredient_list:
    print(f"- {ingredient}")
