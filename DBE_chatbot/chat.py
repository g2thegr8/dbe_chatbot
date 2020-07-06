from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from DBE_Chatbot import run
app = Flask(__name__)


def search(query):
    return run(query)

@app.route("/")
def home():    
    return render_template("html/home.html") 
@app.route("/get")
def get_bot_response():    
    query = request.args.get('msg')    
    return str(search(query)) 
if __name__ == "__main__":    
    app.run()