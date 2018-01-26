# app/frontend.py
from flask import Blueprint, render_template, abort


api_bp = Blueprint('frontend', __name__)


@api_bp.route('/', defaults={'page': 'index.html'})
def serve_pages(page):
    if page in ("index.html", "index"):
        return render_template(
            'index.html',
            title='Home'
        )
    else:
        return abort(404)
