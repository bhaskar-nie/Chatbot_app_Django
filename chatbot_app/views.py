from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from .models import *  # Ensure you are using your models correctly
#from .custom_pos_tagger import CustomPOSTagger  # Import the custom POS tagger

# Initialize the custom POS tagger
#tagger = CustomPOSTagger()

# Create the bot with the required settings
bot = ChatBot(
    'mychatBot',
    read_only=False,
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    # storage_adapter='chatterbot.storage.SQLStorageAdapter',
    # preprocessors=[
    #     'chatterbot.preprocessors.clean_whitespace'
    # ],  
    # tagger=tagger  # Use the custom POS tagger
)

# Training data
list_to_train = [
    "hi",
    "Hi there",
    "What's your name?",
    "I'm BhanuAI, developed by Bhaskar",
    "What is your favourite work?",
    "I love answering your queries"
]

# Train the bot
list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

# Homepage view
def homepage(request):
    return render(request, 'chatbot_app/index.html')

# Get response view
def getResponse(request):
    usermsg = request.GET.get('userMessage')  # userMessage sent as context from index.html
    chatresponse = str(bot.get_response(usermsg))  # Get response from the bot
    return HttpResponse(chatresponse)  # Send the bot's response back to the done() function in index.html
