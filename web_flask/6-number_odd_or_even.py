#!/usr/bin/python3
'''Start a Flask web app'''
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    '''Method that displays "Hello HBNB!"
    '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''fonction that display HBNB
    '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    '''function that displays C + <text>
    '''
    return 'C {}'.format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    '''
    '''
    return 'Python {}'.format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    ''' function that dispaly a number only if its an int'''
    return '{} is a number'.format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def template(n):
    '''
    '''
    return render_template('5-number.html', name=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_odd(n):
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', number=n,
                               name="even")
    else:
        return render_template('6-number_odd_or_even.html', number=n,
                               name="odd")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
