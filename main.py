import os

from flask import Flask, redirect, render_template, request, url_for, flash, session
from werkzeug.utils import secure_filename

app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = "uploads"
app.secret_key = "super secret key"


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, threaded=True, host="0.0.0.0", port=8080)
