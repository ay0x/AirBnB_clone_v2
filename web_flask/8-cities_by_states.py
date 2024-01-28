#!/usr/bin/python3
"""
- Runs Flask web application.
- The application listens on 0.0.0.0, port 5000.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """
    - Displays an HTML page with a list of all State and their cities.
    - States are sorted by name.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    """Starts Flask web application"""
    app.run(host="0.0.0.0", port=5000)
