favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

# The following is a list of people who should take the poll
poll = ["ada", "jen",  "leon", "sarah", "jill", "edward", "mr x", "phil", "albert"]

for user in poll:
    if user in favorite_languages:
        print(f"\nHi {user.title()}, thank you for taking your time to respond the poll")
    else:
        print(f"\n{user.title()}, we ask you to respond our poll")
