# app.py
from flask import Flask, render_template, jsonify, request
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize_speech():
    language = request.form['language']
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.listen(source)

        if language == 'en-US':
            text = recognizer.recognize_google(audio_data, language='en-US')
        elif language == 'en-GB':
            text = recognizer.recognize_google(audio_data, language='en-GB')
        elif language == 'es-ES':
            text = recognizer.recognize_google(audio_data, language='es-ES')
        elif language == 'hi-IN':
            text = recognizer.recognize_google(audio_data, language='hi-IN')
        elif language == 'mr-IN':
            text = recognizer.recognize_google(audio_data, language='mr-IN')
        else:
            return jsonify({'error': 'Unsupported language'}), 400

        return jsonify({'text': text}), 200
    except sr.UnknownValueError:
        return jsonify({'error': 'Could not understand audio'}), 400
    except sr.RequestError as e:
        return jsonify({'error': 'Speech recognition service unavailable'}), 500

if __name__ == '__main__':
    app.run(debug=True)
