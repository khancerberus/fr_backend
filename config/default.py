import os
from os.path import abspath, dirname


BASE_DIR = dirname(dirname(abspath(__file__)))
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False
