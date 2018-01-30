# app/server.py
from flask import Flask, url_for
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mixins import AllFeaturesMixin

Base = declarative_base()


class BaseModel(Base, AllFeaturesMixin):
    __abstract__ = True
    pass


app = Flask(
    __name__,
    template_folder='../static/templates',
    static_folder="../static",
)
app.config.from_object('app.default_config.Config')

db = SQLAlchemy(app, model_class=BaseModel)
ma = Marshmallow(app)
login_manager = LoginManager()
login_manager.init_app(app)


def init_db():
    # Create database and tables
    from app.images import Image
    from app.user import User
    db.create_all()
