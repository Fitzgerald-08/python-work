# In this case, I am using a default value inside the function definition, that means I am giving an argument to
# a parameter directly in the function call, in turn, python interprets this as a positional argument
def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet("coco")
