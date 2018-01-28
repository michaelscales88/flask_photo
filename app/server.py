# app/server.py
from flask import Flask
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


def init_db():
    # Create database and tables
    from app.images import Image
    db.create_all()
