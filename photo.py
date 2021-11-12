import os
import sys

from PIL import Image
from PIL.ExifTags import TAGS


class Photo:

    @staticmethod
    def get_name(path):
        return os.path.splitext(os.path.basename(path))[0]

    @staticmethod
    def get_exif(path):
        img = Image.open(path)
        return img._getexif()

    @staticmethod
    def get_device(exif_data):
        return exif_data[272].rstrip().lstrip()

    @staticmethod
    def get_shutter_speed(exif_data):
        speed = exif_data[33434]
        if speed[0] / speed[1] >= 1:
            ss = speed[0] / speed[1]
            return str(ss)
        else:
            return f'{speed[0]}/{speed[1]}'

    @staticmethod
    def get_f_stop(exif_data):
        aperture = exif_data[33437]
        return str(round(aperture[0] / aperture[1], 1))

    @staticmethod
    def get_iso(exif_data):
        return str(exif_data[34855])

    @staticmethod
    def get_focal_length(exif_data):
        return f'{str(exif_data[37386][0])} mm'
