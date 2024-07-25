#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return ('Hello HBNB!')

@app.route('/hbnb', strict_slashes=False)
def show_HBNB():
    return ('HBNB')

@app.route('/c/<text>', strict_slashes=False)
def return_text(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return ("C {}".format(text))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def return_python_text(text=None):
    if text is None:
        text = 'is cool'
    else:
        # Replace underscores with spaces
        text = text.replace('_', ' ')

    return ("Python {}".format(text))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return (
    """<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: {}</H1>
    </BODY>
</HTML>""".format(n)
            )
    
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        statis = 'even'
    else:
        statis = 'odd'
    return (
    """<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: {} is {}</H1>
    </BODY>
</HTML>""".format(n, statis)
            )

if __name__ == '__main__': 
    app.run(host='0.0.0.0',
            port=5000,
            debug=True)
