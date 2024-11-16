def make_shirt(message="I love Python", size="large"):
    """Display a message confirming size and text to be written on it"""
    print(f"T-shirt size: {size}\nText to be written on it: {message}\n")


make_shirt()
# If there are only default values in the function definition, the position for the keyword argument in the function
# call does not matter at all
make_shirt(size="medium")
make_shirt(message="Python Rocks!", size="small")
