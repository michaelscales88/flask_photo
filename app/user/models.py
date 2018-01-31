# user/models.py
from flask_login import UserMixin

from app import db


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    __repr_attrs__ = ['id']

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.String)

    @classmethod
    def get(cls, id):
        try:
            return cls.query.get(id)
        except KeyError:
            return None
