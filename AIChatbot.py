def show_welcome():
    print("Welcome to the AI Chatbot!")
responses = {
    "hi": "Hello!",
    "how are you": "I am fine.",
    "what is python": "Python is a programming language.",
    "who are you": "I am an AI ChatBot.",
    "what is scripting language": "A scripting language is a programming language that is used to automate tasks.",
    "Bye": "bye! Have a great day!"
}
def get_response(user_input):
    if user_input in responses:
        return responses[user_input]
    else:
        return "Sorry, I don't understand that."
def start_chat():
    show_welcome()
    while True:
        user_input = input("Thanu: ")
        user_input = user_input.lower()
        if user_input in ["bye", "exit", "quit"]:
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print("Bot:", response)
start_chat()



 






