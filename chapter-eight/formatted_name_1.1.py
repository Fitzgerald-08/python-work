def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted"""
    # The following if sentence evaluates to true if a middle name is provided in the function call(1) and then
    # the first_name, middle_name and last_name are combined(2), changed to title case and then returned to the
    # corresponding function call(3)
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"  # <--- (2)
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()  # <--- (3)


musician = get_formatted_name("jimi", "lee")
print(musician)

musician = get_formatted_name("jimi", "hooker", "lee",)  # <--- (1)
print(musician)
