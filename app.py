from flask import Flask
from views import views
from photo import *
from config import secret_key
from os import listdir
from os.path import isfile, join

app = Flask(__name__)
app.secret_key = secret_key
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True, port=8080)
