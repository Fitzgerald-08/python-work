# Base structure to build a program that asks user as many times as they desire
# until they perform a given action

ingredient_list = ["tomato", "lettuce", "ground beef", "cheese"]
final_list = []

prompt = "Select ingredient for your hamburger\n"
prompt += "Enter 'quit once you are finished\n"

ingredient = ""
while ingredient != "quit":
    ingredient = input(prompt)
    if ingredient == "quit":
        break
    elif ingredient in ingredient_list:
        print(f"Adding {ingredient} to the list")
        final_list.append(ingredient)
    else:
        print(f"Sorry, {ingredient} is not available in our list of ingredients")

print("The following resumes the selection of ingredients selected")
for ingredient in final_list:
    print(f"- {ingredient}")
