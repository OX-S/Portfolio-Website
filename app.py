from flask import Flask
from views import views
import config
from photo import *
from math import floor

app = Flask(__name__)
app.secret_key = config.secret_key
app.register_blueprint(views, url_prefix="/")

def prep_photos():
    photos = []
    path = os.path.join(config.idek_what_to_call_this_path, 'static/assets/photographs/')
    print("retard")
    files = [os.path.join(path, f) for f in os.listdir(path)
             if os.path.isfile(os.path.join(path, f))]
    for file in files:
        name = Photo.get_name(file)
        exif = Photo.get_exif(file)
        device = Photo.get_device(exif)
        ss = Photo.get_shutter_speed(exif)
        f_stop = Photo.get_f_stop(exif)
        iso = Photo.get_iso(exif)
        focal_length = Photo.get_focal_length(exif)
        data = (file.replace(os.path.join(config.idek_what_to_call_this_path, 'static/'), ''), name, device, ss, f_stop, iso, focal_length)
        photos.append(data)

    lists = [photos[x:x + (floor(len(photos) / 3)) + 1] for x in range(0, len(photos), floor(len(photos) / 3) + 1)]
    return lists

if __name__ == '__main__':
    config.lists = prep_photos()
    app.run(host="0.0.0.0", debug=True, port=8080)
