#importing ChatBot
from chatterbot import ChatBot
#importing Listtrainer to train chatbot
from chatterbot.trainers import ListTrainer

#create instance chatbot
chatbot = ChatBot("Chatpot")

#create trainer
trainer = ListTrainer(chatbot)
trainer.train(["Hi", 
               "Welcome, friend", ])
trainer.train(["Are you a plant?", 
               "No, I'm the pot below the plant!", ])

#create exit conditions to stop "whileloop"
exit_conditions = (":q", "quit", "exit")

while True :
    query = input("> ")
    if query in exit_conditions :
        break
    else :
        print(f"🪴{chatbot.get_response(query)}")