class Restaurant:
    """Modeling a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print restaurant's name and cuisine's type"""
        print(f"Restaurant: {self.restaurant_name}\n"
              f"Cuisine's type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open"""
        print(f"{self.restaurant_name} is now open")

    def set_number_served(self, customers_served):
        """Number of customers served"""
        self.number_served = customers_served

    def increment_number_served(self, customers_served):
        """Number of customers served in one day of business"""
        self.number_served = customers_served


restaurant = Restaurant("toto", "mexican")
restaurant_information = (f"Restaurant: {restaurant.restaurant_name.title()}\n"
                          f"Cuisine: {restaurant.cuisine_type.title()}")

restaurant = Restaurant("toto", "mexican")

print(f"Number of customers served: {restaurant.number_served}")

restaurant.number_served = 41
print(f"Number of customers served (2nd round): {restaurant.number_served}")

restaurant.set_number_served(69)
print(f"Number of customers served (3rd round): {restaurant.number_served}")

restaurant.increment_number_served(100)
print(f"Final number of customers served in one day of business: {restaurant.number_served}")
