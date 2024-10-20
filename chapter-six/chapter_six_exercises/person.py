person_0 = {
    "first_name": "peter",
    "last_name": "parker",
    "age": 30,
    "city": "new york",
}

person_1 = {
    "first_name": "miles",
    "last_name": "morales",
    "age": 18,
    "city": "new york",
}

person_2 = {
    "first_name": "gwen",
    "last_name": "stacey",
    "age": 20,
    "city": "new york",
}

people = [person_0, person_1, person_2]

for name in people:
    full_name = f"{name["first_name"]} {name["last_name"]}"

    print(f"\nName: {full_name.title()}")
    print(f"\tAge: {name["age"]}")
    print(f"\tLocation: {name["city"]}")
