#!/usr/bin/python3
"""
This module starts a Flask web application with two routes:
- '/' which returns 'Hello HBNB!'
- '/hbnb' which returns 'HBNB'
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns a greeting message 'Hello HBNB!' when accessing the root path.
    """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns 'HBNB' when accessing the '/hbnb' path.
    """
    return ('HBNB')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
