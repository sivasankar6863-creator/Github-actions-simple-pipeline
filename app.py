#test app
from flask import Flask, jsonify, request

app = Flask(__name__)

# Basic route
@app.route("/")
def home():
    return "<h1>Hello, Flask!</h1>"

# Dynamic route with a URL parameter
@app.route("/user/<name>")
def greet_user(name):
    return f"Hello, {name}!"

# JSON API route (GET and POST)
@app.route("/api/data", methods=["GET", "POST"])
def handle_data():
    if request.method == "POST":
        data = request.get_json()
        return jsonify({"received": data}), 201
    return jsonify({"status": "success", "message": "Send a POST request with JSON"})

if __name__ == "__main__":
    app.run(debug=True)
