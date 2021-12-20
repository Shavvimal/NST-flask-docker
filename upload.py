from flask import Flask, render_template, request, send_file, send_from_directory
# if you encounter dependency issues using 'pip install flask-uploads'
# try 'pip install Flask-Reuploaded'
from flask_uploads import UploadSet, configure_uploads, IMAGES
# the pretrained model
from model import load_img, combine
import os 

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

# path for saving uploaded images
app.config['UPLOADED_PHOTOS_DEST'] = './static/img'
configure_uploads(app, photos)

# professionals have standards :p
@app.route('/home', methods=['GET', 'POST'])
def home():
    welcome = "Hello, World !"
    return welcome

# the main route for upload and prediction
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo1' in request.files and 'photo2' in request.files:

        content = photos.save(request.files['photo1'])
        style = photos.save(request.files['photo2'])
        
        content_image = load_img('./static/img/'+content)
        style_image = load_img('./static/img/'+style)


        final_image = combine(content_image, style_image)
        
        final_image.save('./static/img/final_image.jpg', "JPEG")

        os.remove('./static/img/'+content)
        os.remove('./static/img/'+style)

        return send_from_directory('./static/img/', 'final_image.jpg', as_attachment=False)
    # web page to show before the POST request containing the image
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
