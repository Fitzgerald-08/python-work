def describe_city(city, country="iceland"):
    """Display the name of a city and the country it is found"""
    print(f"{city.title()} is in {country.title()}\n")


describe_city("Reykjavik")
describe_city("warsaw", "poland")
describe_city("riga", "latvia")
