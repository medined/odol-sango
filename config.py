import os

class Config(object):
    SECRET_KEY = os.environ.get('ODOL_SECRET_KEY') or 'secret-key-345234sdfs2342'
