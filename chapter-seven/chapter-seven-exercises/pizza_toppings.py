prompt = "\nThink of the toppings you want in your pizza and type 'quit' when you are ready to order"
prompt += "\nEnter toppings: "  # <--- (2) !!Both lines 1 and 2!!

message = ""
while message != "quit":  # <--- (1)
    # This one is pretty simple, while message is not equal to quit, run the following code (1), which will ask the
    # user for the toppings they want in their pizza (2), then, the "if" test, evaluates whether the input is "quit" (3)
    # and if it is, the while loop stops there (4), if it isn't, it will print a message with the topping they added
    # and run once again (5)
    message = input(prompt)  # !!REMEMBER THAT THE ORDER OF THE PROMPT DOES MATTER
    if message == "quit":  # <--- (3)
        break  # <--- (4)
    else:
        print(f"We'll add {message}")  # <--- (5)
