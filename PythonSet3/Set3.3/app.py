from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return 'File uploaded successfully'

@app.route('/download')
def download_file():
    return render_template('download.html', files=os.listdir(UPLOAD_FOLDER))

@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory(directory=UPLOAD_FOLDER, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
