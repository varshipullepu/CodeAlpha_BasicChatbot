import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data (in case it's not already downloaded)
nltk.download('punkt')

# Define the pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name\??",
        ["I am a chatbot created by Varshitha.",]
    ],
    [
        r"how are you\??",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["No problem", "It's alright",]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Take care.",]
    ],
    [
        r"(.*) created you\??",
        ["Varshitha created me using Python and NLTK.",]
    ],
    [
        r"what can you do\??",
        ["I can chat with you, respond to some questions, and more!",]
    ],
    [
        r"(.*)",  # Catch-all pattern for anything else
        ["I'm not sure how to respond to that. Can you ask something else?"]
    ]
]

# Creating the chatbot using pairs and reflections
chatbot = Chat(pairs, reflections)

# Function to start the chat
def start_chat():
    print("Hi, I'm your chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == "bye":
            print("Goodbye! Have a nice day.")
            break
        else:
            response = chatbot.respond(user_input)
            if response:
                print(response)
            else:
                print("I didn't understand that. Can you try again?")

# Start the chatbot
if __name__ == "__main__":
    start_chat()
