#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template

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

@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Prints string"""
    return f'Python {text.replace("_", " ")}'

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Prints only number"""
    return f'{n} is a number'

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Prints a number on html template"""
    return render_template('5-number.html', num=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Prints if a number is odd or even on html template"""
    quotient, remainder = divmod(n, 2)
    parity = "even" if remainder == 0 else "odd"
    return render_template('6-number_odd_or_even.html', num=n, parity=parity)

if __name__ == "__main__":
    """Starts Flask web application"""
    app.run(host="0.0.0.0", port=5000)
