# In this version of pets.py, I have explicitly given a value to the parameters 'animal_type' and 'pet_name' in the
# function call
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet(animal_type="dog", pet_name="coco")
