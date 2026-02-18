print("Chatbot starting...")
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file
DB_CONN = os.getenv("DB_CONN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# MongoDB connection (Cosmos DB)
from pymongo import MongoClient

# connect to Cosmos DB
client = MongoClient(DB_CONN)
db = client['chatbotdb']         # database name
chats_collection = db['chats']   # container (collection) name

# OpenAI client
from openai import OpenAI
openai_client = OpenAI(api_key=OPENAI_API_KEY)

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    bot_reply = "Hello! You said: " + user_msg
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
