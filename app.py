import os
from flask import Flask
from views import views
from config import secret_key
from generate import *

app = Flask(__name__)
app.secret_key = secret_key
app.register_blueprint(views, url_prefix="/")

photo_lists = generate_photos()
artwork_list = generate_artwork()

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)

