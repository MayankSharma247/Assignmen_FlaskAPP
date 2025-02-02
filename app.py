from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask App!"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name.capitalize()}!"

@app.route("/api/data")
def api_data():
    return jsonify({"id": 1, "name": "Flask App", "version": "1.0.0"})

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

