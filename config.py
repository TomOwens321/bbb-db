# from https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one
# config.py

class Config(object):
    """
      Common configs
    """
    SECRET = 'mysecret'
    SQLALCHEMY_DATABASE_URI='sqlite:///bbb/db/dev.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    TESTING = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}