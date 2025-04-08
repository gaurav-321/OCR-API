# OCR-API 📄

OCR-API is a Python-based Optical Character Recognition (OCR) application built using Flask. It allows users to upload images and extract text from them using the Google OCR API, with the detected text highlighted within the image.

## Features 🔥

- **Image Upload:** Easily upload images for text extraction.
- **Text Extraction:** Extracts text from uploaded images using the Google OCR API.
- **Text Highlighting:** Highlights the detected text within the original image.
- **JSON Output:** Provides extracted text and bounding box coordinates in JSON format.

## Installation 🔧

To get started, follow these steps to install the necessary dependencies:

1. Clone the repository:
   ```bash
   git clone https://github.com/gag3301v/OCR-API.git
   cd OCR-API
   ```

2. Install Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage 📦

### Running the Application

To run the OCR-API application, execute the following command:

```bash
python main.py
```

The server will start on `http://127.0.0.1:5000/`. You can now upload images via the web interface.

### Example Code Snippet

Here’s how you can use the OCR-API to extract text from an image:

```python
import requests
import json

def requestOCR(image_path):
    with open(image_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    url = "https://vision.googleapis.com/v1/images:annotate"
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "requests": [
            {
                "image": {"content": encoded_image},
                "features": [{"type_": "TEXT_DETECTION"}]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Example usage
ocr_result = requestOCR("path/to/your/image.jpg")
print(json.dumps(ocr_result, indent=2))
```

## Configuration 🛠️

The application uses environment variables to configure settings. Here’s an example of how to set them:

```bash
export FLASK_APP=main.py
export FLASK_ENV=development
```

## Tests 🧪

To run the tests for the OCR-API, execute the following command:

```bash
python -m unittest discover tests
```

Ensure you have the necessary test files in a `tests` directory.

## Project Structure 📁

The project structure is organized as follows:

```
OCR-API/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── upload.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── logo.png
├── README.md
├── requirements.txt
└── main.py
```

## Contributing 🙌

We welcome contributions from the community! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Made with ❤️ by gag3301v**