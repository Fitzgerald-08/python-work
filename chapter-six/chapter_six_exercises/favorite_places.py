favorite_places = {
    "ronald": {
        "place": "hawaii",
    },
    "mike": {
        "place": "japan",
    },
    "anthony": {
        "place": "thailand",
    },
}

for friend, place in favorite_places.items():
    print(f"{friend.title()} would like to travel to:")
    print(f"\t{place["place"].title()}")

for friend in favorite_places:
    place = favorite_places[friend]

    print(f"\n{friend.title()}")
    print(f"\t{place["place"].title()}")
