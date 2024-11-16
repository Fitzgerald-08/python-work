def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info["first_fact"] = first
    user_info["last_fact"] = last
    return user_info


user_profile = build_profile("albert", "einstein",
                             location="princeton",
                             field="physics",)
print(user_profile)
