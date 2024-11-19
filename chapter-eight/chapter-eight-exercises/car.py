def car_info(manufacturer, model, color="red", **specs):
    """Display information about a car"""
    specs["manufacturer"] = manufacturer
    specs["model"] = model
    specs["color"] = color
    return specs


car = car_info("bmw", "i4", color="white", features="hybrid", number="one")
car_two = car_info("bmw", "i4", features="hybrid", number="one")
for specs, features in car.items():
    print(f"{specs.title()}: {features}")

print()
for specs, features in car_two.items():
    print(f"{specs.title()}: {features}")
