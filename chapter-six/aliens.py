# Make an empty list of 30 aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

for alien in aliens[:1]:
    if alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15

# Show me the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show me how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")