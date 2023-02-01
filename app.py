from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
   {
        "inputs": 3,
        "category": "Music[Best Boy Band On The Planet!😎]",
        "word": "BTS"
    },
    {
        "inputs": 10,
        "category": "✨Most Wonderful Teacher Of Mine✨(Ma'am You don't even need to guess)",
        "word": "Ms.Adeline"
    },
    {
        "inputs": 5,
        "category": "Your Favourite Student(😂)",
        "word": "Savya"
    },
]


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-template")
def get_template():
  return jsonify({
        "status": "success",
        "word": random.choice(templates)
  })

if __name__ == '__main__':
  app.run()
