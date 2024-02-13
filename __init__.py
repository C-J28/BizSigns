from flask import *
from flask_wtf import *
from wtforms import *
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired

import os
import magic
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '#36859'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file_types(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=('GET', 'POST'))
@app.route('/home', methods=('GET', 'POST'))
def home():
    return render_template('index.html')

@app.route('/hub', methods=('GET', 'POST'))
def hub():
    name = request.cookies.get('userID')
    print("Text: ")
    print(name)

    return render_template('hub.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('login.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    path = 'uploads/'

    if file and allowed_file_types(file.filename):
        file.save(path + file.filename)
        flash('file Uploaded and saved')
        return redirect(url_for("upload"))
    else:
        flash('Invalid file')
        return redirect(url_for("upload"))
    
@app.route("/base")
def base():
    return render_template('base.html')

# Manage Cookies
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
   
        resp = make_response('Setting the Cookie')
        resp.set_cookie('userID', user)
   
        return resp 
    


if __name__ == '__main__':
    app.run(debug=True)