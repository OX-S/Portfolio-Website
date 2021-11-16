from flask import Flask
from views import views
from config import secret_key

app = Flask(__name__)
app.secret_key = secret_key
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)
