def city_country(city, country):
    """Display the name of a city and its name"""
    city_names = f"{city}, {country}"
    return city_names.title()


cityCountry = city_country("moscow", "russia")
print(cityCountry)

cityCountry = city_country("madrid", "spain")
print(cityCountry)

cityCountry = city_country("prague", "czechia")
print(cityCountry)
