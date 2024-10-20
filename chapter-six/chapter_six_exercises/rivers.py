rivers = {
    "nile": "egypt",
    "the amazon": "peru, colombia, brazil",
    "the yangtze": "china",
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

print("\nList of the three major rivers:")
for river in rivers.keys():
    print(river.title())

print("\nCountries where each river runs through:")
for country in rivers.values():
    print(country.title())
