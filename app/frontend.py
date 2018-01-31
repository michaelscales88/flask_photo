# app/frontend.py
from flask import Blueprint, render_template, abort
from flask_login import login_required

from .user.utitilities import login


api_bp = Blueprint('frontend', __name__)


@api_bp.route('/', defaults={'page': 'upload.html'})
@api_bp.route('/<string:page>')
def serve_pages(page):
    if page in ("index.html", "index"):
        return render_template(
            'index.html',
            title='Home'
        )
    elif page in ("login.html", "login"):
        # return render_template(
        #     'login.html',
        #     title='Login'
        # )
        return login()
    elif page in ("upload.html", "upload"):
        return serve_login_pages(page)
    else:
        return abort(404)


@login_required
def serve_login_pages(page):
    if page in ("upload.html", "upload"):
        return render_template(
            'upload.html',
            title='Upload'
        )
    else:
        return abort(404)
