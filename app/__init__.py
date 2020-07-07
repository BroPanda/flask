from flask import Flask
from config import DevConfig
from .posts.views import posts
from .owners.views import owners

app = Flask(__name__)

app.config.from_object(DevConfig)
app.register_blueprint(posts, url_prefix='/posts')
app.register_blueprint(owners, url_prefix='/owners')

from app import views
