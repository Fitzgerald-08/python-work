prompt = "Enter your age or enter '0' to stop the loop: "
active = True

while active:
    age = int(input(prompt))
    if age == 0:
        active = False
    elif age <= 3:
        print("You can enter for free")
    elif age <= 12:
        print("The cost of the ticket is $10")
    else:
        print("The cost of the ticket is $15")
