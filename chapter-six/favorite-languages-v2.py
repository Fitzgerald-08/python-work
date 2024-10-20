favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
    if len(languages) >= 2:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is:")
        for language in languages:  # <---- (1) Remove this and follow the instructions below
            # (2) When working with lists, it is strictly necessary to use a for loop to "loop" through that list,
            # if you try to print a value by itself as in the code below, it will show an error

            # (3) print(f"{languages.title()}"

            print(f"\t{language.title()}")
            # (4) To summarize, if you are using a list inside a dictionary, and you want to print the value held by "x"
            #  key, you must use a for loop, otherwise, it is not necessary
