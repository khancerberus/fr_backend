from flask import Flask


def generate_app(settings='config.development'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(settings)

    register_blueprints(app)

    return app

def register_blueprints(app:Flask):
    from app.home import home_bp
    app.register_blueprint(home_bp)
