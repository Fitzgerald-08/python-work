def make_album(artist_name, album, number_of_songs=None):
    """Define a function that displays at least three different albums, the name of the artist and, if applicable
    the number of songs on the album"""
    album_info = {
        "artist": artist_name,
        "album": album,
        "songs on the album": number_of_songs,
    }
    return album_info


album_var = make_album("jello", "sorry")
album_var2 = make_album("dox", "alone forever", number_of_songs=8)
album_var3 = make_album("next-door rock", "rocking at midnight", number_of_songs=4)

print(album_var)
print(album_var2)
print(album_var3)

# Adding a bit of difficulty to this test.
# Since it is a dictionary, I will access the data and play with it

# First, the dictionary corresponding to album_var
print()
for category, artist_info in album_var.items():
    print(f"{category}: {artist_info}")

# Second
print()
for category, artist_info in album_var2.items():

    full_info = f"{category.title()}: {artist_info}"
    print(full_info)

# And third
print()
for category, artist_info in album_var3.items():
    full_info = f"{category.title()}: {artist_info}"
    print(full_info)
