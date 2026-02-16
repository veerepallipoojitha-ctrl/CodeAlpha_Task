print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hi! Nice to meet you 😊")

    elif user_input == "how are you":
        print("Bot: I'm fine, thank you! How can I help you?")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a great day 👋")
        break

    else:
        print("Bot: Sorry, I didn't understand that.")
