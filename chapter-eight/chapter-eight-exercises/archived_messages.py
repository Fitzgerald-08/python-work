def send_messages(text_messages, sent_messages):
    """Print each text message
    Move each text message to the list sent_messages
    """
    while text_messages:
        moved_messages = text_messages.pop()
        print(f"Message: {moved_messages}")
        sent_messages.append(moved_messages)


messages_list = ["Hello there!", "Howdy", "How you feeling?", "Hey there!"]
messages_sent = []
send_messages(messages_list[:], messages_sent)


print("In this part of the exercise, the list messages_list will keep its values thanks of the [:] slice notation")
print(f"\nThis is the list messages_list:\n{messages_list}")

print("\nThe messages_sent list will make use of the values used in message_list without affecting the latter")
print(f"This is the list messages_sent:\n{messages_sent}")
