army_0 = []
army_1 = []

# I still don't get why I have to assign one name inside the for loop and another one when I assign a key to the
# dictionary
for troop_info in range(15):
    # Here I will create my fleet of Roys, who are in charge fo destroying the world, they will be deployed in
    # different parts of the world
    new_troop = {
        "race": "roy",
        "roll": "infantry",
        "location": "stockholm",
    }
    army_0.append(new_troop)

for troop_info in range(30):
    new_troop = {
        "race": "popis",
        "roll": "support",
        "location": "stockholm"
    }
    army_1.append(new_troop)

# In case I want to print only the first 3, 5 , 7 items from the list I have created I just have to use the following
# function, it would look something like the following:

# for troop in army_0[:5] | Remove the next line and uncomment this one
for troop in army_0[:1]:
    print(f"\nType of troop: {troop["race"].title()}")
    print(f"Roll: {troop["roll"].title()}")
    print(f"Where it will be located: "
          f"{troop["location"].title()}")

print(f"\nNumber of units deployed already: {len(army_0)}")

print(f"\n\nThe following troops will accompany the troops"
      f" from above")

# There's probably a function to tackle the next problem, but for now, I'll just do it with the knowledge I have
# already acquired. I created another list where I stored another type of troops because I cannot put them in the
# same list I put the troops of type "roy", since I cannot retrieve the information
for troop in army_1[:1]:
    print(f"\nType of troop: {troop["race"].title()}")
    print(f"Roll: {troop["roll"].title()}")
    print(f"Where it will be located: "
          f"{troop["location"].title()} (alongside 'Roys')")

print(f"Number of troops deployed already: {len(army_1)}")
