from flask import Flask, jsonify
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__) 

@app.route("/")
def home():
    return jsonify({"response": "Hello world!!"})

if __name__ == '__main__':
    app.run(port=int(getenv("PORT", 8080)))

