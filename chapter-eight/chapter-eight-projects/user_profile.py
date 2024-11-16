def arbitrary_example(name, last_name, **user):
    """Create a user profile and neatly display the information"""
    user["first_name"] = name
    user["last_name"] = last_name
    return user


# By using an arbitrary keyword argument, **user in this case, you are basically creating a dictionary containing
# every piece of information residing in the function call, if we were to use arbitrary keyword arguments along
# positional arguments, the latter will go first and arbitrary arguments last
arbitrary_var = arbitrary_example("alexandro", "marquez",
                                  food="hamburger",
                                  color="black",
                                  langue="english",
                                  programming_language="python", )

for key, value in arbitrary_var.items():
    print(f"{key.title()}: {value.title()}")
