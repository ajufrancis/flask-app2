from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from PIL import Image
import librosa
import soundfile as sf
import nltk
nltk.download('punkt')

app = Flask(__name__)

# Configure the upload folder
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('data_file')
        if not file or file.filename == '':
            return 'No file selected.'
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return redirect(url_for('display_file', filename=filename))
    return render_template('index.html')

@app.route('/display/<filename>')
def display_file(filename):
    file_ext = filename.rsplit('.', 1)[1].lower()
    file_url = url_for('static', filename='uploads/' + filename)
    content = None

    if file_ext == 'txt':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(file_path, 'r') as f:
            content = f.read()

    return render_template('display.html', filename=filename, file_ext=file_ext, file_url=file_url, content=content)

@app.route('/preprocess/<filename>', methods=['POST'])
def preprocess(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    preprocessed_filename = 'preprocessed_' + filename
    preprocessed_path = os.path.join(app.config['UPLOAD_FOLDER'], preprocessed_filename)
    file_ext = filename.rsplit('.', 1)[1].lower()

    if file_ext in ['png', 'jpg', 'jpeg', 'gif']:
        img = Image.open(file_path).convert('L')
        img.save(preprocessed_path)
    elif file_ext == 'txt':
        with open(file_path, 'r') as f:
            text = f.read().lower()
        with open(preprocessed_path, 'w') as f:
            f.write(text)
    elif file_ext in ['wav', 'mp3']:
        y, sr = librosa.load(file_path, sr=None)
        y_normalized = librosa.util.normalize(y)
        sf.write(preprocessed_path, y_normalized, sr)
    else:
        return 'Unsupported file type for preprocessing.'
    
    return redirect(url_for('show_preprocessed', filename=preprocessed_filename))

@app.route('/preprocessed/<filename>')
def show_preprocessed(filename):
    file_ext = filename.rsplit('.', 1)[1].lower()
    file_url = url_for('static', filename='uploads/' + filename)
    content = None

    if file_ext == 'txt':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(file_path, 'r') as f:
            content = f.read()

    return render_template('preprocess.html', filename=filename, file_ext=file_ext, file_url=file_url, content=content)

@app.route('/augment/<filename>', methods=['POST'])
def augment(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    augmented_filename = 'augmented_' + filename
    augmented_path = os.path.join(app.config['UPLOAD_FOLDER'], augmented_filename)
    file_ext = filename.rsplit('.', 1)[1].lower()

    if file_ext in ['png', 'jpg', 'jpeg', 'gif']:
        img = Image.open(file_path)
        img_rotated = img.rotate(45)
        img_rotated.save(augmented_path)
    elif file_ext == 'txt':
        with open(file_path, 'r') as f:
            text = f.read()
        augmented_text = text + "\nThis is an augmented sentence."
        with open(augmented_path, 'w') as f:
            f.write(augmented_text)
    elif file_ext in ['wav', 'mp3']:
        y, sr = librosa.load(file_path, sr=None)
        y_fast = librosa.effects.time_stretch(y, rate=1.5)
        sf.write(augmented_path, y_fast, sr)
    else:
        return 'Unsupported file type for augmentation.'
    
    return redirect(url_for('show_augmented', filename=augmented_filename))

@app.route('/augmented/<filename>')
def show_augmented(filename):
    file_ext = filename.rsplit('.', 1)[1].lower()
    file_url = url_for('static', filename='uploads/' + filename)
    content = None

    if file_ext == 'txt':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(file_path, 'r') as f:
            content = f.read()

    return render_template('augment.html', filename=filename, file_ext=file_ext, file_url=file_url, content=content)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)

