from flask import Flask, render_template, request
import os

from analyzer import analyze_chart

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['image']

    path = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(path)

    result = analyze_chart(path)

    return render_template(
        'result.html',
        result=result,
        image=path
    )

if __name__ == '__main__':

    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )
