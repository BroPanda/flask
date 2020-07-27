from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from .posts.views import posts
from .owners.views import owners

app.register_blueprint(posts, url_prefix='/posts')
app.register_blueprint(owners, url_prefix='/owners')

from app import views
