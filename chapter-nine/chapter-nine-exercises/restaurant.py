""""""


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

