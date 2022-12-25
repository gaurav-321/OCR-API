# OCR API
A simple application to extract text from images using OCR (Optical Character Recognition).

## Description
This application is built using Python and Flask. It allows users to upload an image and extract the text present in it using the Google OCR API. The application also highlights the detected text in the image.

## Requirements
Python 3
Flask
OpenCV
requests
json
## Usage
Clone the repository

Copy code
```
git clone https://github.com/[username]/OCR-API.git
```
Install the required packages
```
pip install Flask opencv-python requests json
```
Replace the API key in the code with your own API key obtained from Google Cloud Console
Run the application
```
python app.py
```
Open the application in your web browser at **http://localhost:8080**
Upload an image and click on submit to extract the text from the image
## Output
The output will be the text present in the image and the image with the detected text highlighted. The output is displayed on the same page as the input image.

## Note
The API key used in this application is from the Google Cloud Console and has a usage limit. To use the application without any limitations, obtain your own API key from the Google Cloud Console and replace it in the code.




