from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired

import os
import magic

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file_types(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=('GET', 'POST'))
@app.route('/home', methods=('GET', 'POST'))
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    path = 'uploads'

    if file and allowed_file_types(file.filename):
        file.save(path + file.filename)
        return 'file Uploaded and saved'
    else:
        return 'Invalid file'


@app.route("/base")
def base():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)