prompt = "Enter your age: "

while True:
    age = int(input(prompt))
    if age < 3:
        print("You can enter for free")
    elif age <= 12:
        print("The cost of the ticket is $10")
    else:
        print("The cost of the ticket comes to $15")
