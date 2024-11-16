def send_messages(text_messages, sent_messages):
    """Print each text message
    Move each text message to the list sent_messages
    """
    while text_messages:
        moved_messages = text_messages.pop()
        print(f"Message: {moved_messages}")
        sent_messages.append(moved_messages)


message_list = ["Hello there!", "Howdy", "How you feeling?", "Hey there!"]
messages_sent = []
send_messages(message_list, messages_sent)

print(f"\nThis is the list message_list:\n{message_list}")
print(f"This is the list sent_messages:\n{messages_sent}")
