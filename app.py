from flask import Flask, request, render_template, send_file
from PIL import Image
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress():
    if 'image' not in request.files:
        return "No file part", 400
    file = request.files['image']
    quality = int(request.form.get('quality', 70))  # Default quality is 70

    if file.filename == '':
        return "No selected file", 400

    img = Image.open(file)
    output_filename = "compressed_" + file.filename
    img.save(output_filename, optimize=True, quality=quality)

    return send_file(output_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
