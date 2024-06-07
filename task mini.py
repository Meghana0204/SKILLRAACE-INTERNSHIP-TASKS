import random

# Dictionary of responses
responses = {
    "hello": ["Hello! How can I assist you today?", "Hi! What's on your mind?", "Hey! What can I help you with?"],
    "hi": ["Hi! What's on your mind?", "Hey! What can I help you with?", "Hello! How can I assist you today?"],
    "how are you": ["I'm doing well, thanks! How about you?", "I'm good, thanks for asking!", "I'm great, thanks!"],
    "what is your name": ["My name is Chatty, nice to meet you!", "I'm Chatty, your friendly chatbot!", "My name is Chatty, I'm here to help!"],
    "default": ["I didn't understand that. Can you please rephrase?", "Sorry, I'm not sure what you mean. Can you explain?", "I'm not sure I understand. Can you please clarify?"]
}

def get_response(message):
    message = message.lower()
    for key in responses.keys():
        if key in message:
            return random.choice(responses[key])
    return random.choice(responses["default"])

def chatbot():
    print("Welcome to Chatty! I'm here to help with any questions you may have.")
    while True:
        message = input("You: ")
        response = get_response(message)
        print("Chatty: " + response)

if __name__ == "__main__":
    chatbot()
