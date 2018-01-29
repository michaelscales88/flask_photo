# app/backend.py
from flask import Blueprint
from flask_restful import Api


api_bp = Blueprint('backend', __name__)
api = Api(api_bp)

from .images.api import ImageAPI, ImagesAPI

# Register the endpoint to the api
api.add_resource(ImageAPI, "/image")
api.add_resource(ImagesAPI, '/get-images')

