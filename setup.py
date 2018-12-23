from flask import Flask, url_for, render_template
from flask import request, abort, redirect, session, escape
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Index Page</h1>'

@app.route('/hello/')
@app.route('/hello/<username>')
def hello(username=None):
    return render_template('hello.html', username=username)