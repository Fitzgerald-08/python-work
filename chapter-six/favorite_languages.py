favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",

}

friends = ["phil", "sarah"]
if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll\n")

for name in favorite_languages:
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language.title()}")

