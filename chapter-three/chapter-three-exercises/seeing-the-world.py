places = ["Japan", "Spain", "United Kingdom", "Italy", "Poland"]

print(places)

# Print places list in both alphabetical order and the original
print(sorted(places))
print(places)

# Print list in reverse-alphabetical order
print(sorted(places, reverse=True))

# Once again, showing the list remains in its original order
print(places)

# Using reverse to reverse the order of the list
places.reverse()
print(places)
# Back to the original order
places.reverse()
print(places)

# Printing list alphabetical order... PERMANENTLY!!
places.sort()
print(places)

# Finally, printing the list in reverse-alphabetical order... PERMANENTLY!!
places.sort(reverse=True)
print(places)
