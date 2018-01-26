# app/server.py
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mixins import AllFeaturesMixin

Base = declarative_base()


class BaseModel(Base, AllFeaturesMixin):
    __abstract__ = True
    pass


app = Flask(
    __name__,
    instance_relative_config=True,
    instance_path='/tmp'
)
app.config.from_object('backend.default_config.Config')
CORS(app)

db = SQLAlchemy(app, model_class=BaseModel)


def init_db():
    # Create database and tables
    db.create_all()
