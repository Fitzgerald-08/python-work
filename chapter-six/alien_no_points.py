alien_0 = {"color": "green", "speed": "slow"}

# The get() method is used in case the key you are asking does not exist
point_value = alien_0.get("points", "No point value assigned.")
print(point_value)
