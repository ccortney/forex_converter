from flask import Flask, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

debug = DebugToolbarExtension(app)

@app.route('/')
def form():
    return render_template('form.html')