# app/frontend.py
from flask import Blueprint
from flask_restful import Api


api_bp = Blueprint('frontend', __name__)
api = Api(api_bp)
