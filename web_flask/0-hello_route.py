#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hbnb():
    """Prints text"""
    return "Hello HBNB!"


if __name__ == "__main__":
    """Starts Flask web application"""
    app.run(host="0.0.0.0")
