import os
from config import idek_what_to_call_this_path
from artwork import *
from photo import *
from math import floor

def generate_photos():
    photos = []
    path = os.path.join(idek_what_to_call_this_path, 'static/assets/photographs/')

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
        data = (file.replace(os.path.join(idek_what_to_call_this_path, 'static/'), ''), name, device, ss, f_stop, iso, focal_length)
        photos.append(data)

    return [photos[x:x + (floor(len(photos) / 3)) + 1] for x in range(0, len(photos), floor(len(photos) / 3) + 1)]

def generate_artwork():
    artworks = []

    files = [f for f in os.listdir(os.path.join(idek_what_to_call_this_path, 'static/assets/artwork/'))
             if os.path.isfile(os.path.join(os.path.join(idek_what_to_call_this_path, 'static/assets/artwork/', f)))]
    for file in files:
        art_piece = Artwork(file)
        artworks.append(art_piece.get_list())
    return artworks
