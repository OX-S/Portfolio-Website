from flask import Flask
from views import views
from photo import *
from config import secret_key

app = Flask(__name__)
app.secret_key = secret_key
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    exif = Photo.get_exif("static//assets//photographs//nycbeach.jpeg")
    print(Photo.get_device(exif))
    print(Photo.get_shutter_speed(exif))
    print(Photo.get_f_stop(exif))
    print(Photo.get_iso(exif))
    print(Photo.get_focal_length(exif))
    app.run(debug=True, port=8080)
