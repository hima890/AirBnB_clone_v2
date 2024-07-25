#!/usr/bin/python3
"""
This module starts a Flask web application and defines a route
for the root ('/') path.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns a greeting message when accessing the root path.
    """
    return ('Hello HBNB!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
