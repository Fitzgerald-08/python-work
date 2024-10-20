favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

# The sorted() method helps us sort the keys, (it could also be values), it has a very straight forward function
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking our poll")

print("\nThe following languages have been mentioned:")
# Thanks to the set() method, we avoid repeating printing the same values over and over again
for language in set(favorite_languages.values()):
    print(language.title())
