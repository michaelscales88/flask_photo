from app import db


class Image(db.Model):

    __tablename__ = 'image'
    __repr_attrs__ = ['id', 'title', 'description', 'filename', 'visible']

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.TEXT)
    filename = db.Column(db.String)
    visible = db.Column(db.Boolean, default=True)
