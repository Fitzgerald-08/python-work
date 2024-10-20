responses = {}
polling_userName = "Please, introduce your name: "
polling_response = "If you could visit one place in the world, where would you go? "

polling_active = True

while polling_active:
    user_name = input(polling_userName)
    user_response = input(polling_response)
    responses[user_name] = user_response

    repeat = input("Would you like to let someone else respond? (yes/no) ").lower()
    if repeat == "no":
        polling_active = False

print("\n---------------------\n"
      "+    Poll Results   +\n"
      "---------------------")

for user, response in responses.items():
    print(f"{user.title()} responded he would like to visit {response.title()}")

