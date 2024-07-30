#!/usr/bin/python3
"""Flask web application to display states and cities"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()

@app.route('/states', strict_slashes=False)
def states():
    """Display all states"""
    try:
        states = storage.all("State").values()
        states = sorted(states, key=lambda x: x.name)
        return render_template('9-states.html', states=states)
    except SQLAlchemyError as e:
        return f"An error occurred: {e}", 500

@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Display a state and its cities by id"""
    try:
        states = storage.all("State")
        state = next((s for s in states.values() if s.id == id), None)
        if state:
            state.cities = sorted(state.cities, key=lambda x: x.name)
            return render_template('9-states.html', state=state)
        else:
            return render_template('9-states.html', state=None)
    except SQLAlchemyError as e:
        return f"An error occurred: {e}", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
