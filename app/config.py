import os

class Config(object):
    key = os.environ.get('SECRET_KEY') or 'placeholder-key'