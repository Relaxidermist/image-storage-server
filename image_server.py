from fileinput import filename
import os
from flask import Flask, render_template_string, request
from flask import render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/ingram/Pictures/slideshow/'

app = Flask(__name__, static_folder=UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.debug = True

@app.route("/")
def serve_landing_page():
    return render_template('index.html')

@app.route("/about")
def serve_about_page():
    return render_template('about.html')

#TODO Need to not have the path hardcoded in
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
    """
    Serve a grid of photos that are in the upload folder
    """
    files = os.listdir(UPLOAD_FOLDER)
    print(app.static_folder)
    p = ""
    for f in files:
        img_src = "\"{{{{url_for('static', filename = '{}')}}}}\"".format(f)
        p = p + " <image src =" + img_src + " height=\"240\"/>"
        
    p = '<!DOCTYPE html> <html><body> ' + p + '</body></html>'

    app.logger.info(p)

    return render_template_string(p)

@app.route("/delete/<filename>")
def delete_image(filename):
    try:
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        app.logger.info(path)
        os.remove(path)
        response = "<p>" + filename + " deleted</p>"
    except FileNotFoundError:
        response = "<p>" + filename + " not found</p>"
    
    return response
