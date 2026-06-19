from import1 import import2

class ChatBot:
    def __init__(self):
        self.name = None
    
    def greet(self):
        self.name = input("Chatbot: Hello! What's your name?\nYou: ")
        print(f"Chatbot: Nice to meet you, {self.name}!")

    def tell_joke(self):
        return "Why don’t scientists trust atoms? Because they make up everything!"

    def give_weather(self):
        return "It's sunny with a high chance of clouds in the evening."

    def tell_time(self):
        return f"The current time is {datetime.now().strftime('%H:%M')}."

    def respond(self, user_input):
        if 'joke' in user_input:
            return self.tell_joke()
        elif 'weather' in user_input:
            return self.give_weather()
        elif 'time' in user_input:
            return self.tell_time()
        else:
            return "I’m not sure how to respond to that."

    def chat(self):
        self.greet()
        
        while True:
            user_input = input("You: ").lower()
            
            if 'exit' in user_input:
                print(f"Chatbot: Goodbye, {self.name}!")
                break
            
            response = self.respond(user_input)
            print(f"Chatbot: {response}")

# Create and start the chatbot
my_chatbot = ChatBot()
my_chatbot.chat()
