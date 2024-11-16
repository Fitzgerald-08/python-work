def data_dictionary(first_name, last_name):
    """Save user's data into a dictionary"""
    user_info = {
        first_name: last_name,
    }
    return user_info


while True:
    f_name = input("Introduce your name: ")
    if f_name == "q":
        break

    l_name = input("Introduce your last name: ")
    if l_name == "q":
        break

    information_dictionary = data_dictionary(f_name, l_name)
    for name, lName in information_dictionary.items():
        full_name = f"{name.title()} {lName.title()}"
        print(full_name)
