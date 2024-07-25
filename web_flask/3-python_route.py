#!/usr/bin/python3
"""
This module starts a Flask web application with four routes:
- '/' which returns 'Hello HBNB!'
- '/hbnb' which returns 'HBNB'
- '/c/<text>' which returns 'C ' followed by the value of the text variable,
with underscores replaced by spaces.
- '/python/(<text>)' which returns 'Python ', followed by the value of the
text variable or the default 'is cool', with underscores replaced by spaces.
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
def show_HBNB():
    """
    Returns 'HBNB' when accessing the '/hbnb' path.
    """
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def return_text(text):
    """
    Returns 'C ' followed by the value of the text variable,
    with underscores replaced by spaces,
    when accessing the '/c/<text>' path.
    """
    text = text.replace('_', ' ')  # Replace underscores with spaces
    return ("C {}".format(text))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def return_python_text(text):
    """
    Returns 'Python ' followed by the value of the text variable
    or the default 'is cool',with underscores replaced by spaces,
    when accessing the '/python/' or '/python/<text>' path.
    """
    text = text.replace('_', ' ')  # Replace underscores with spaces
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            )
