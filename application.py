"""
This app shows how to use paths in Flask web application
"""
from flask import Flask
import os

application = Flask(__name__)

# http://localhost:8080/ displays "Welcome!"
@application.route('/')
def index():
    return '<H1>Welcome!</H1>'


# http://localhost:8080/person/Jane displays "Welcome Jane!". Try to use different names.
@application.route('/person/<fname>')
def greeting1(fname):
    return '<H1>Welcome ' + fname + '!</H1>'


# http://localhost:8080/person/Jane/Doe displays first and last name provided
@application.route('/person/<fname>/<lname>')
def greeting2(fname, lname):
    output = '<H1>Welcome ' + fname + ' ' + lname + '!</H1>'
    return output


# http://localhost:8080/square/4 - you have to use a number to get a result
@application.route('/square/<int:anumber>')
def square(anumber):
    square = anumber * anumber
    output = f'<H1>{anumber} * {anumber} = {square} </H1>'
    return output


if __name__ == "__main__":
    application.run(port=int(os.environ.get('PORT')))
