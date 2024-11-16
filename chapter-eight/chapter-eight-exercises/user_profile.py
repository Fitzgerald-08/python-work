def build_profile(name, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info["first_name"] = name
    user_info["last_name"] = last
    return user_info


user_information = build_profile("Alexandro", "Marquez",
                                 location="Mexico",
                                 field="Software Engineering",
                                 specialization="Networking and Security", )

for first, second in user_information.items():
    whole_info = f"{first}: {second}"
    print(whole_info)
