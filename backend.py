from flask import Flask, render_template, request, send_from_directory
from gtts import gTTS
import os

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('frontend.html')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form.get('freeform')
    output_file = "output.mp3"
    text_to_speech(text, output_file)
    os.system(f"start {output_file}") 
    return f'Text received and processed: {text}'

@app.route('/output.mp3')
def audio(filename):
    return send_from_directory('static', filename)

@app.route('/')
def index():
    return render_template('output.html')

def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    print(f'Audio content written to file "{output_file}"')


if __name__ == "__main__":
    app.run(debug=True)

