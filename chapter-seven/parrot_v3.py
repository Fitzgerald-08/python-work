prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message != "quit":
        print(message)
    else:
        print(message)
