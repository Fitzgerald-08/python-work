def make_album(album_artist, album_title):
    """Define a program that prompts the user for an album's artist and its title"""
    album_info = f"{album_artist}: {album_title}\n"
    return album_info


while True:
    print("Enter the following info about an artist")
    print("You can enter 'q' whenever you want to quit the program")

    al_artist = input("Enter name of the artist: ").lower()
    if al_artist == "q":
        break

    al_title = input("Enter title of the album: ").lower()
    if al_title == "q":
        break

    answer = input("Would you like to keep giving answers? (yes/no)").lower()
    if answer == "no":
        break

    formatted_info = make_album(al_artist, al_title)
    print(formatted_info)
