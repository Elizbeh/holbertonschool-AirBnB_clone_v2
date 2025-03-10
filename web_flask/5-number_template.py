#!/usr/bin/python3
'''A script that starts a Flask web application'''

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    '''Method display Hello HHBNB!'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''method displays
    '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    '''method replace and displays
    '''
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    '''method replace and displays Python + <text>
    '''
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    '''Method displays'''
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def template(n):
    '''Function that displays template'''
    return render_template("5-number.html", num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
