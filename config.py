import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # wtform
    SECRET_KEY = os.environ.get('ODOL_SECRET_KEY') or 'secret-key-345234sdfs2342'
    # database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
