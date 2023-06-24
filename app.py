# app.py
from flask import Flask, request, jsonify, render_template
import openai
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('transcribe.html')


UPLOAD_FOLDER = 'C:/Users/W10/Desktop/WhisperAudioTranscript/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    if 'file' not in request.files:
        return jsonify({"error": "no file"}), 400
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb') as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        
    return jsonify(transcript)

if __name__ == "__main__":
    app.run(debug=True)