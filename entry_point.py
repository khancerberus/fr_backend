import os

from app import generate_app


settings = os.environ.get('APP_SETTINGS_MODULE')
application = generate_app(settings)
