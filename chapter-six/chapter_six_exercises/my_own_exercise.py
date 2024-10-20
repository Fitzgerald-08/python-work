users_name = {
    "fitzgerald": "alex",
    "ellen": "trixie",
    "josh": "roy",
    "sebastian": "ludovico",
}

for username in users_name.keys():
    real_name = users_name[username]
    print(f"{username.title()}: {real_name.title()}")
