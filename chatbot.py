def chatbot():
    print("ChatBot: Hi! I'm a simple chatbot. Type 'bye' to end the chat.")
    
    while True:
        user_input = input("You: ")
        
        if user_input == "bye":
            print("ChatBot: Goodbye! Have a nice day!")
            break

        elif user_input == "hello" or user_input == "hi":
            print("ChatBot: Hello! How can I help you?")
        elif user_input == "how are you":
            print("ChatBot: I'm just a bot, but I'm here to help you!")
        elif user_input == "what is your name" or user_input == "your name":
            print("ChatBot: I'm ChatBot, your virtual assistant!")
        elif user_input == "h elp":
            print("ChatBot: I'm here to assist you! Ask me anything.")
        else:
            print("ChatBot: I'm sorry, I don't understand. Can you ask something else?")

chatbot()
