import os


class Config:
    SECRET_KEY = os.urandom(24)  # Generate a random session key

    DEBUG = True
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    PACKAGEDIR = os.path.dirname(BASEDIR)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(PACKAGEDIR, 'tmp/local_app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = os.path.join(PACKAGEDIR, 'tmp/images/')
    ALLOWED_EXTENSIONS = (
        'jpg',
        'jpeg',
        'png',
        'gif',
    )

