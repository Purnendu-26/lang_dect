from flask import Flask, render_template, request
from lingua import Language, LanguageDetectorBuilder

# Initialize Flask app
app = Flask(__name__)

# Initialize Lingua language detector for multiple languages
detector = LanguageDetectorBuilder.from_all_languages().build()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_language():
    text = request.form['text'].strip()

    # Handle empty text input
    if len(text) == 0:
        result = "Error: Please enter some text to detect the language."
    else:
        detected_language = detector.detect_language_of(text)
        if detected_language:
            result = f"Detected Language: {detected_language.name}"
        else:
            result = "Could not detect the language."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

