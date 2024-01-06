from flask import Flask, render_template

import os

app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
@app.route("/home", methods=('GET', 'POST'))
def home():
    return render_template("index.html")

@app.route("/template")
def menu():
    return render_template('template.html')

if __name__ == '__main__':
    app.run()