languages = ["Spanish", "English", "French", "Japanese", "Italian", "German", "Polish", "Chinese"]


print("\nThe number of languages i would like to learn in my life are at least the following:")
print(f"{len(languages)}\n")


# --> !!Always remember that SORTED is a function, while REVERSE and SORT are methods, notice the difference¡¡ <--

print("Print list in reverse-alphabetical order:")
print(sorted(languages, reverse=True))

print("\nPrint list in reverse order:")
languages.reverse()
print(f"{languages}")

print("\nPrint list in alphabetical order, but this is a permanent change:")
languages.sort()
print(languages)
