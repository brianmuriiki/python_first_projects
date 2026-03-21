from flask import Flask, render_template, request
import pickle
import numpy as np
import re
from scipy.sparse import hstack

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Preprocessing
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    return text

def uppercase_ratio(text):
    return sum(1 for c in text if c.isupper()) / len(text)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    message = request.form["message"]

    clean = clean_text(message)
    text_vec = vectorizer.transform([clean])

    features = np.array([[
        len(message),
        len(message.split()),
        message.count('!'),
        sum(c.isdigit() for c in message),
        uppercase_ratio(message),
        1 if "http" in message else 0
    ]])

    final_input = hstack([text_vec, features])

    prediction = model.predict(final_input)[0]

    result = "SPAM 🚨" if prediction == 1 else "HAM ✅"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)