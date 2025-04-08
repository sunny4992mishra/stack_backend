from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r") as f:
        return json.load(f)

@app.route("/top-tags")
def top_tags():
    return jsonify(load_json("top_tags_per_month.json"))

@app.route("/question-volume")
def question_volume():
    return jsonify(load_json("monthly_question_volume.json"))

@app.route("/unique-tags")
def unique_tags():
    return jsonify(load_json("unique_tags_per_month.json"))

@app.route("/top-tags-year")
def top_tags_year():
    return jsonify(load_json("top_tags_per_year.json"))

if __name__ == "__main__":
    app.run(debug=True,port=5000)