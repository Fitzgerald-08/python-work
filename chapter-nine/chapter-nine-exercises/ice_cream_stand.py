class Restaurant:
    """Modeling a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print restaurant's name and cuisine's type"""
        print(f"Restaurant: {self.restaurant_name}\n"
              f"Cuisine's type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open"""
        print(f"{self.restaurant_name} is now open")


class IceCreamStand(Restaurant):
    """Just modeling an Ice Cream stand"""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Initialize attributes for the ice cream stand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def return_flavors(self):
        """Return flavors neatly formatted"""
        print("This is the list of available flavors\n")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


# Instead of using a list inside the IceCreamStand init method, I decided to use a list outside the classes, and use it
# as a parameter for the "stand" instance, as shown below
flavors_one = ["chocolate", "vanilla", "strawberry", "hershey"]

stand = IceCreamStand("hola k ase", "ice cream stand", flavors_one)
stand.return_flavors()
