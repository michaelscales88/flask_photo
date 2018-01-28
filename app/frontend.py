# app/frontend.py
from flask import Blueprint, render_template, abort


api_bp = Blueprint('frontend', __name__)


@api_bp.route('/', defaults={'page': 'upload.html'})
@api_bp.route('/<string:page>')
def serve_pages(page):
    if page in ("upload.html", "index"):
        return render_template(
            'index.html',
            title='Home'
        )
    elif page in ("upload.html", "upload"):
        return render_template(
            'upload.html',
            title='Upload'
        )
    else:
        return abort(404)
