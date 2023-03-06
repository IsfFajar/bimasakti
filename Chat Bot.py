#importing ChatBot
from chatterbot import ChatBot

#create instance chatbot
chatbot = ChatBot("Chatpot")

#create exit conditions to stop "whileloop"
exit_conditions = (":q", "quit", "exit")

while True :
    query = input("> ")
    if query in exit_conditions :
        break
    else :
        print(f"🪴{chatbot.get_response(query)}")