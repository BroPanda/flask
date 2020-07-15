class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Dub1Sub2@localhost/flask_test'


class DevConfig(Config):
    DEBUG = True
