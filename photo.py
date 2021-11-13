import os

from PIL import Image
from PIL.ExifTags import TAGS
from fractions import Fraction


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
            if type(exif_data[33434]) is tuple:
                speed = exif_data[33434]
                if speed[0] / speed[1] >= 1:
                    ss = speed[0] / speed[1]
                    return f'{str(ss)} s'
                else:
                    return f'{speed[0]}/{speed[1]} s'
            else:
                if exif_data[33434] > 1:
                    return f'{exif_data[33434]} s'
                else:
                    return f'{str(Fraction(exif_data[33434]))} s'
        except (TypeError, KeyError) as e:
            return '-'

    @staticmethod
    def get_f_stop(exif_data):
        try:
            if type(exif_data[33437]) is tuple:
                aperture = exif_data[33437]
                return f'𝑓{str(round(aperture[0] / aperture[1], 1))}'
            else:
                return f'𝑓{exif_data[33437]}'
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
            if type(exif_data[37386]) is tuple:
                return f'{str(round(exif_data[37386][0]/exif_data[37386][1]))} mm'
            else:
                return f'{round(exif_data[37386])} mm'
        except (TypeError, KeyError) as e:
            return '-'
