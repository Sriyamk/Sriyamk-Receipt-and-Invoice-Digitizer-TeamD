from flask import Flask, request, jsonify

app = Flask(__name__)


# Home route
@app.route("/")
def home():
    return "Flask API is running!"


# Dashboard route
@app.route("/dashboard")
def dashboard():
    return "Hello Flask API!"


# Add two numbers
@app.route("/add", methods=["POST"])
def add():
    data = request.json
    a = data.get("a")
    b = data.get("b")
    return jsonify({"sum": a + b})


# Get user info
@app.route("/user/<username>")
def user(username):
    return jsonify({"user": username})


if __name__ == "__main__":
    app.run(debug=True)
