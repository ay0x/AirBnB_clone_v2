#!/usr/bin/python3
"""
- Runs Flask web application.
- The application listens on 0.0.0.0, port 5000.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """
    - Displays an HTML page with a list of all States.
    - States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    - Displays an HTML page with states and their ID.
    - States are sorted by name.
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    """Starts Flask web application"""
    app.run(host="0.0.0.0", port=5000)
