import json
import os
from base64 import b64encode
import cv2
import flask
import requests
from flask import Flask, redirect, render_template, request, url_for, flash, session, jsonify, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = "uploads"
app.secret_key = "super secret key"


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        files = request.files.to_dict()
        data = []
        for file in files:
            files[file].save(os.path.join(app.config['UPLOAD_FOLDER'], files[file].filename))
            res = requestOCR(os.path.join(app.config['UPLOAD_FOLDER'], files[file].filename))
            data.append([files[file].filename, res.json()['responses'][0]['textAnnotations'][1:]])
            frame = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], files[file].filename))
            for word in res.json()['responses'][0]['textAnnotations'][1:]:
                ver = word['boundingPoly']['vertices']
                cv2.rectangle(frame, (ver[0]["x"], ver[0]["y"]), (ver[2]["x"], ver[2]["y"]), (0, 0, 255), 1)
            cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], files[file].filename), frame)
        return jsonify(data)

    else:
        return render_template("index.html")


@app.route('/upload')
def get_image():
    filename = os.path.join(app.config['UPLOAD_FOLDER'], request.args.get('file'))
    return send_file(filename, mimetype='image/jpg')


def makeImageData(imgpath):
    img_req = None
    with open(imgpath, 'rb') as f:
        ctxt = b64encode(f.read()).decode()
        img_req = {
            'image': {
                'content': ctxt
            },
            'features': [{
                'type': 'DOCUMENT_TEXT_DETECTION',
                'maxResults': 1
            }]
        }
    return json.dumps({"requests": img_req}).encode()


def requestOCR(imgpath):
    ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
    api_key = "AIzaSyBb-LvJr_MuCCqqnx7BqKHc5-20lUoS5CE"
    imgdata = makeImageData(imgpath)
    response = requests.post(ENDPOINT_URL,
                             data=imgdata,
                             params={'key': api_key},
                             headers={'Content-Type': 'application/json'})
    return response


if __name__ == "__main__":
    app.run(debug=True, threaded=True, host="0.0.0.0", port=8080)
