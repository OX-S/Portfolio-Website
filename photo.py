import os

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
        try:
            return exif_data[272].rstrip().lstrip()
        except (TypeError, KeyError) as e:
            return '-'

    @staticmethod
    def get_shutter_speed(exif_data):
        try:
            speed = exif_data[33434]
            if speed[0] / speed[1] >= 1:
                ss = speed[0] / speed[1]
                return str(ss)
            else:
                return f'{speed[0]}/{speed[1]} s'
        except (TypeError, KeyError) as e:
            return '-'

    @staticmethod
    def get_f_stop(exif_data):
        try:
            aperture = exif_data[33437]
            return f'𝑓{str(round(aperture[0] / aperture[1], 1))}'
        except (TypeError, KeyError) as e:
            return '-'

    @staticmethod
    def get_iso(exif_data):
        try:
            return f'ISO {str(exif_data[34855])}'
        except (TypeError, KeyError) as e:
            return '-'

    @staticmethod
    def get_focal_length(exif_data):
        try:
            return f'{str(round(exif_data[37386][0]/exif_data[37386][1]))} mm'
        except (TypeError, KeyError) as e:
            return '-'
