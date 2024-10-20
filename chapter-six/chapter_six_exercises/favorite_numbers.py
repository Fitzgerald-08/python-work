favorite_numbers = {
    "ludovico": [27, 1],
    "trixie": [9, 2],
    "roy": [13, 41],
    "coco": [21, 90],
    "popis": [5, 9],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is:")
    for number in numbers:
        print(f"{number}")

# In this case, this solution is not very effective, since it will print the values along the square brackets
for name in favorite_numbers:
    number = favorite_numbers[name]

    print(f"These are {name.title()}' favorite numbers:")
    print(f"{number}")
