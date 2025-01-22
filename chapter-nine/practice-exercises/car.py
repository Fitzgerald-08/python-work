class Car:
    """Model a simple car"""

    def __init__(self, make, model, year, fuel_level=100):
        """Initialize the attributes for a car"""
        self.make = make
        self.model = model
        self.year = year
        self.fuel_level = fuel_level

    def start(self):
        """The car has been started"""
        return ("- The car has started\n"
                f"\t- Fuel level {self.fuel_level}")

    def drive(self):
        """Decrease fuel level once the car has started"""
        decreased_fuel_level = self.fuel_level * .10
        self.fuel_level -= decreased_fuel_level

        return f"Car fuel decreased to {self.fuel_level}"

    def refuel(self):
        """Restore fuel back to 100%"""
        self.fuel_level = 100

        return self.fuel_level

    def display_info(self):
        """Show current car information"""
        return (f"Car make: {self.make.upper()}\n"
                f"Car model: {self.model}\n"
                f"Model Year: {self.year}")


first_car = Car("bmw", "i4", 2024)

print(first_car.start())
print(f"\n- {first_car.drive()}")
print(f"\n- {first_car.drive()}")
print(f"\n- {first_car.drive()}")
print(f"\n- Car fuel restored to {first_car.refuel()}")
print(f"\n{first_car.display_info()}")
