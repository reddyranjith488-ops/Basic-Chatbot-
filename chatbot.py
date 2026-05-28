print(" Basic Chatbot")
print("Type 'bye' to end the chat.\n")

while True:

    user_input = input("You: ").lower()

    # Predefined responses
    if user_input == "hello":
        print("Bot: Hi!")

    elif user_input == "how are you":
        print("Bot: I'm fine, thanks!")

    elif user_input == "what is your name":
        print("Bot: I'm a Python Chatbot.")

    elif user_input == "what can you do":
        print("Bot: I can chat with you and respond to simple questions.")
        
    elif user_input == "what is ai":
        print("Bot: AI stands for Artificial Intelligence, which is the simulation of human intelligence in machines.")

    elif user_input == "what is python":
        print("Bot: Python is a popular programming language known for its simplicity and versatility.")

    elif user_input == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")