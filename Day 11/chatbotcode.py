import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot. You can call me ChatBot.",]
    ],
    [
        r"how are you ?",
        ["I'm good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry",]
    ],
    [
        r"I (want|need) (.*)",
        ["Why do you %1 %2?",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Nice talking to you. Goodbye!"]
    ],
]

def chatbot():
    print("Hi, I'm ChatBot. How can I assist you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download("punkt")
    chatbot()