import os
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
    return render_template("index.html")

@app.route('/', methods=["POST"])
def uploadFile():

    if request.method == 'POST':
        _img = request.files['file-uploaded']
        filename = _img.filename
        #allowed_file(filename)
        _img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        return render_template('index.html', success=True)
    
@app.route('/show_file')
def displayImage():

    img_file_path = session.get('uploaded_img_file_path', None)
    if img_file_path.split(".")[-1] in ("mp4", "mov"):
        return render_template('show_file.html', user_image=img_file_path, is_image = False, is_show_button=True)
    else:
        return render_template('show_file.html', user_image = img_file_path, is_image= True, is_show_button=True)
    

@app.route('/detect_object')
def detectObject():

    uploaded_image_path = session.get('uploaded_img_file_path', None)
    output_image_path, response, file_type = blur_it_up(uploaded_image_path)

    file_type = 'image'
    if file_type == "image":
        return render_template('show_file.html',  user_image=output_image_path, is_image= True, is_show_button=False)
    else:
        return render_template('show_file.html',  user_image= output_image_path, is_image= False, is_show_button=False)



if __name__ == '__main__':
    app.run(debug=True)