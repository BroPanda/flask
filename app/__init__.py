from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

from config import DevConfig

from .posts.views import posts
from .owners.views import owners

app.config.from_object(DevConfig)
app.register_blueprint(posts, url_prefix='/posts')
app.register_blueprint(owners, url_prefix='/owners')

from app import views
