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

    from bbb.routes.home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    from bbb.routes.genus import genus as genus_blueprint
    app.register_blueprint(genus_blueprint)
    from bbb.routes.species import species as species_blueprint
    app.register_blueprint(species_blueprint)
    from bbb.routes.flora import flora as flora_blueprint
    app.register_blueprint(flora_blueprint)
    from bbb.routes.fauna import fauna as fauna_blueprint
    app.register_blueprint(fauna_blueprint)
    from bbb.routes.family import family as family_blueprint
    app.register_blueprint(family_blueprint)

    return app