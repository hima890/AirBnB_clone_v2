#!/usr/bin/python3
"""Flask web application that displays states and cities"""

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

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays a list of states and their cities"""
    try:
        states = storage.all("State").values()
        states = sorted(states, key=lambda x: x.name)
        for state in states:
            state.cities = sorted(state.cities, key=lambda x: x.name)
        
        return render_template('8-cities_by_states.html', states=states)
        
    except SQLAlchemyError as e:
        return f"An error occurred: {e}", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
