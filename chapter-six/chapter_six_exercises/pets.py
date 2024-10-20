pet_0 = {
    "pet": "snake",
    "race": "python",
    "age": 12,
    "owner": "roy",
}

pet_1 = {
    "pet": "dog",
    "race": "chihuahua",
    "age": 24,
    "owner": "tom",
}

pet_2 = {
    "pet": "cat",
    "race": "egyptian",
    "age": 30,
    "owner": "kate"
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"\nPet: {pet["pet"].title()}")
    print(f"Race: {pet["race"].title()}")
    print(f"Age(in months): {pet["age"]}")
    print(f"Owner's name: {pet["owner"].title()}")
