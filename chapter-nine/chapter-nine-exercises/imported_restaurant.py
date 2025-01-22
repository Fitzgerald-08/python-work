from restaurant import Restaurant


my_restaurant = Restaurant("Willi's", "Polish")
my_restaurant.describe_restaurant()

# I decided to call this method, it only has to be used if the restaurant is open, though (Obviously).
# So I can put it inside an if statement to raise this text if work_hours is inside the current_hour (for example)
my_restaurant.open_restaurant()
