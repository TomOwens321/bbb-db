from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    migrate = Migrate(app, db)

    from bbb import models
    
    from bbb.views import home as home_blueprint
    app.register_blueprint(home_blueprint)
    from bbb.views import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    from bbb.views import genus as genus_blueprint
    app.register_blueprint(genus_blueprint)
    from bbb.views import species as species_blueprint
    app.register_blueprint(species_blueprint)

    return app