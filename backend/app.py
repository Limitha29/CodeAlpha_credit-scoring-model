from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)

# Allow frontend requests
CORS(app)

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return "Credit Scoring API Running..."


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    income = float(data["income"])
    debt = float(data["debt"])
    credit_score = float(data["credit_score"])

    prediction = model.predict(
        [[income, debt, credit_score]]
    )

    if prediction[0] == 1:
        result = "✅ Loan Approved"
    else:
        result = "❌ Loan Rejected"

    return jsonify({
        "result": result
    })


if __name__ == "__main__":
    app.run(debug=True)