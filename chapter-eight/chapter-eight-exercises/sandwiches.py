def make_sandwich(ingredients):
    """Ask a user to enter ingredients for a sandwich"""
    return ingredients


def modify_ingredients(value):
    """Remove or add a selected ingredient from list"""
    if value == "y" or value == "yes" or value == "yep" or value == "yeah":
        prompt_two = "What would you like to do?"
        prompt_two += "\n'r' to remove or 'a' to add an ingredient:\n"
        answer = input(prompt_two).lower()

        if answer == "r":
            remove_prompt = "Select ingredient to remove: "
            remove_ingredient = ""
            while remove_ingredient != "q":
                remove_ingredient = input(remove_prompt)
                if remove_ingredient not in ingredient_list and remove_ingredient != "q":
                    remove_active = True
                    while remove_active:
                        print(ingredient_list)
                        print("Sorry, there's no such ingredient")
                        remove_ingredient = input(remove_prompt)
                    if remove_ingredient in ingredient_list:
                        ingredient_list.remove(remove_ingredient)
                elif remove_ingredient == "q":
                    exit()
                elif remove_ingredient in ingredient_list:
                    ingredient_list.remove(remove_ingredient)

        elif answer == "a":
            print()
            add_prompt = "Enter new ingredient:\n"
            new_ingredient = ""
            active = True
            while active:
                new_ingredient = input(add_prompt)
                if new_ingredient == "q":
                    active = False
                ingredient_list.append(new_ingredient)

            print("Your sandwich with the following selection will be ready soon:")
            for ingredient in ingredient_list:
                print(f"-{ingredient}")

        else:
            answer = input(prompt_two).lower()

    elif value == "n" or value == "no" or value == "nop" or value == "nope":
        exit()
    return ingredient_list


prompt = "Enter desired ingredients\n"
prompt += "Press 'q' once you are finished:\n"
ingredient_list = []

ingredient = ""
while ingredient != "q":
    ingredient = input(prompt)

    if ingredient != "q":
        ingredient_list.append(ingredient)

    selected_ingredients = make_sandwich(ingredient_list)

print("\nThis is the list of ingredients selected:\n")
for ingredient in selected_ingredients:
    print(f"- {ingredient}")

possible_answers = ["y", "yes", "yep", "yeah", "n", "no", "nop", "nope"]

print()
selection_prompt = "Would you like to modify your selection?\n"

modify_list = ""
while modify_list not in possible_answers:
    modify_list = input(f"{selection_prompt}")
    if modify_list in possible_answers:
        final_list = modify_ingredients(modify_list)

print(final_list)
