import os
from flask import Flask, request
from flask import render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/ingram/Pictures/slideshow/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.debug = True

@app.route("/")
def serve_landing_page():
    return render_template('home.html')

@app.route("/about")
def serve_about_page():
    return render_template('about.html')

@app.route("/upload", methods=["GET","POST"])
def serve_upload_page():
    if request.method == "GET":
        return render_template('upload.html')
    elif request.method == "POST":
        f = request.files['new_image']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))             
        return render_template('uploaded.html')

@app.route("/gallery")
def serve_update_page():
    return render_template('gallery.html')

@app.route("/contact")
def serve_contact_page():
    return render_template('contact.html')