cities = {
    "madrid": {
        "country": "spain",
        "population": 90000000,
        "fact": "lorem ipsum 1",
    },
    "paris": {
        "country": "france",
        "population": 60000000,
        "fact": "lorem ipsum 2",
    },
    "berlin": {
        "country": "germany",
        "population": 120000000,
        "fact": "lorem ipsum 3",
    },
}

for city, info in cities.items():
    country = info["country"].title()
    population = info["population"]
    fact = info["fact"]

    print(f"\nCountry: {country}")
    print(f"Capital city: {city.title()}")
    print(f"Estimated population: {population}")
    print(f"Interesting facts about this city: {fact.capitalize()}")
