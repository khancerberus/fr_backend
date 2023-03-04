from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def generate_app(settings='config.development'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(settings)

    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)

    return app

def register_blueprints(app:Flask):
    from app.home import home_bp
    app.register_blueprint(home_bp)
