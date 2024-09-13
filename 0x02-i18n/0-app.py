#!/usr/bin/env python3
""" Basic flask app """
from flask import Flask, render_template


# Instantiate the Flask application object
app = Flask(__name__)

@app.route('/')
def index():
    """ Returns the index page """
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run(host="5000", port="0.0.0.0", debug=True)
