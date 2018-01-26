# app/backend.py
from flask import Blueprint
from flask_restful import Api


api_bp = Blueprint('backend', __name__)
api = Api(api_bp)


# Register the endpoint to the api
# api.add_resource(TaskListAPI, "/get-tasks")

