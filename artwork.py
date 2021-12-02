import os

class Artwork:

    def __init__(self, file):
        self.path =  os.path.join('assets/artwork/', file)
        self.name = file.split('(')[0].replace('_',' ').title()
        self.median = file.split("(",1)[1].rsplit(".",1)[0][:-1].title()

    def get_path(self):
        return self.path

    def get_name(self):
        return self.name

    def get_median(self):
        return self.median

    def get_list(self):
        return [self.get_name(), self.get_path(), self.get_median()]