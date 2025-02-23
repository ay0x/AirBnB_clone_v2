#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Prints string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Prints string"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Prints string"""
    return f'C {text.replace("_", " ")}'


if __name__ == "__main__":
    """Starts Flask web application"""
    app.run(host="0.0.0.0", port=5000)
