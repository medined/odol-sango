import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # wtform
    SECRET_KEY = os.environ.get('ODOL_SECRET_KEY') or 'secret-key-345234sdfs2342'
    # database
    SQLALCHEMY_DATABASE_URI = os.environ.get('ODOL_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Target Suger Numbers
    TARGET_MORNING = os.environ.get('ODOL_TARGET_MORNING') or 100
    TARGET_EVENING = os.environ.get('ODOL_TARGET_EVENING') or 140
