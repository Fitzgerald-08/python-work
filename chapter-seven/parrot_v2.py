# This code belong to the prompt that will be displayed to the user, and it will be waiting for
# an answer
prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# If the answer is different to quit, the program will keep on showing the same prompt until I type:
# 'quit'
message = ""
# In this example, I am using the message variable so that the while loop has something to work with, otherwise, I
# would not be able to work with it, once inside the loop, I store the
while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)
