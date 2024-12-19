def identify_guest(identity):
    """Identify a user by their name and decide whether they can order or they have to be kicked out"""

    bad_users = ["andrea", "betty", "cecilia", "danna", "ernesto", "federico", "gonzalo"]

    print("Before getting started, please confirm your identity\n"
          "Enter 'quit' whenever you want to exit the program")

    while True:
        name = input("Enter name: ").lower()

        if name in bad_users:
            while True:
                evil_status = input("Are you evil? (y/n)\n")
                if evil_status == "y":
                    print("Sorry, you are not allowed in")
                    break
                    # break will 'break out' of the while loop and then the program will continue where I left
                    # This is different from using exit(), which will directly exit the program with no further...
                elif evil_status == "n":
                    return name
                else:
                    print("Sorry, I couldn't catch that, what did you say?")
        elif name == "quit":
            break
        else:
            return name

