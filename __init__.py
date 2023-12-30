from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired

import os

from file_uploader import get_uploaded_file

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images/'


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route("/", methods=('GET', 'POST'))
@app.route("/home", methods=('GET', 'POST'))
def home():
    form = UploadFileForm()  # Instantiate your form class here
    if form.validate_on_submit():
        pass
    return render_template("index.html", form=form)

@app.route("/routine1")
def routine1():
    image_folder = os.path.join(app.static_folder, 'images/routine1')
    num_images = len([f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))])
    return render_template('menu.html', num_images=num_images)

if __name__ == '__main__':
    app.run()