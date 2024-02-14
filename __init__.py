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

@app.route('/navigation', methods = ['POST', 'GET'])
def check_navbar():
    if request.method == 'POST':
        if request.form.get('btn1') == 'Home':
            return home()
        
        elif request.form.get('btn2') == 'Sign In':
            return render_template('signin.html')
        
        elif request.form.get('btn3') == 'About':
            return render_template('about.html')
        
        elif request.form.get('btn4') == 'Contact':
            return render_template('contact.html')

    elif request.method == 'GET':
        return render_template('index.html', form=form)

@app.route('/', methods=('GET', 'POST'))
@app.route('/home', methods=('GET', 'POST'))
def home():
    return render_template('index.html')

@app.route('/navpage') 
def navpage(): 
    return render_template('navpage.html') 

@app.route('/hub', methods=('GET', 'POST'))
def hub():
    name = request.cookies.get('userID')

    return render_template('hub.html')

@app.route('/signin', methods=('GET', 'POST'))
def login():
    return render_template('signin.html')

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