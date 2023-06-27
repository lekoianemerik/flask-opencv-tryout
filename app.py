import os, shutil
from flask import Flask, render_template, request, session
from utils import *
app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
OUTPUT_FOLDER = os.path.join('static', 'output')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'xyz'
#app.config["MONGO_URI"] = "mongodb://localhost:27017/"
os.path.dirname("../templates")



@app.route('/')
def main():
    print('HERE1')
    if request.method == 'GET':
        print('HERE2')
        print(UPLOAD_FOLDER)
        print(os.listdir(UPLOAD_FOLDER))
        for filename in os.listdir(UPLOAD_FOLDER):
            filepath = (os.path.join(UPLOAD_FOLDER, filename))
            try:
                os.remove(filepath)
                print(f'deleted {filepath}')
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (filepath, e))
        for filename in os.listdir(OUTPUT_FOLDER):
            filepath = (os.path.join(OUTPUT_FOLDER, filename))
            try:
                os.remove(filepath)
                print(f'deleted {filepath}')
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (filepath, e))

    return render_template('index.html')

@app.route('/', methods=["POST"])
def uploadFile():
    
    if request.method == 'POST':
        _img = request.files['file-uploaded']
        filename = _img.filename
        _img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        return render_template('index.html', success=True)

    

    
@app.route('/show_file', methods=['GET', 'POST'])
def displayImage():

    img_file_path = session.get('uploaded_img_file_path', None)
    output_image_path, response, file_type = blur_it_up(img_file_path)

    print(output_image_path)
    return render_template('show_file.html', image_uploaded=True, original_image=img_file_path, transformed_image=output_image_path)    


if __name__ == '__main__':
    app.run(debug=True)