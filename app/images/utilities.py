from flask import current_app, abort, send_from_directory
from werkzeug.exceptions import BadRequest

from app import ma
from .models import Image


def allowed_file(filename):
    return (
        '.' in filename and
        filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']
    )


def send_or_404(file):
    try:
        return send_from_directory(current_app.config['UPLOAD_FOLDER'], file)
    except BadRequest:
        return abort(404)


class ImageSchema(ma.ModelSchema):
    class Meta:
        model = Image
