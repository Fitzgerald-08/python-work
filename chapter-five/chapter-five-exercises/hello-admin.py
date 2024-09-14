users = ["admin", "alex", "coco", "malcolm", "dewey"]
# Delete all the values above and see what happens when you run the code

if users:
    for user in users:
        if user == "admin":
            print(f"Hello {user.title()}, would you like to see a status report?")
        elif user == "coco":
            print(f"I'll keep an eye on you {user.title()}, so don´t try anything suspicious")
        else:
            print(f"Hello {user.title()}, thank you for logging in")
else:
    print("We need to find some users")
