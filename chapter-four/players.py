players = ["charles", "martina", "michael", "florence", "eli"]

print("Here are the first players on my team")
for player in players[:3]:
    print(player.title())

# Exercise part of "Try it yourself" on page 65
print(f"\nThe first three items in the list are: {players[:3]}")
print(f"Three items from the middle of the list are: {players[1:4]}")
print(f"The last three items in the list are: {players[-3:]}")
