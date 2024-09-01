fav_romcom = "Ijirenaide, Nagatoro"
print("Is best_romcom == 'Ijirenaide, Nagatoro'? I predict True, obviously True!!")
print(fav_romcom == "Ijirenaide, Nagatoro")

laptop = "Lenovo"
print("\nIs laptop == 'Acer'? I predict False")
print(laptop == "Acer")

language = "Spanish"
print("\nIs language == 'Spanish'? I think it is true")
print(language == "Spanish")


# Second test, part of "More conditional tests" exercise

name = "Alex"
print("\nI predict the output will be True")
print(name.lower() == "alex")

# Numerical Tests

magic_number = 10
if magic_number == 10:
    print("\nThe magic number is indeed 10")

second_number = 15
if second_number != 18:
    print("The second magic number is not 18, but 15")

third_number = 30
fourth_number = 40
if third_number >= 20 and fourth_number > 30:
    print("\nYes, both conditions are true")

if third_number > 12 or fourth_number > 50:
    print("\nOne of the conditions is true")

if third_number == 30:
    print("\nYep!")

list_name = ["Lenovo", "Acer", "Asus", "Dell"]
my_laptop = "Macbook"
if my_laptop not in list_name:
    print(f"\nI am sorry, buy my {my_laptop} laptop is not in the list")

cars = ["Toyota", "Honda", "Volkswagen", "Nissan", "Jeep"]
dream_car = "Honda"
if dream_car in cars:
    print("\nThis brand is in the list")
