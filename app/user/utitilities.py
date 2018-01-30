# user/utilities.py
from flask import redirect, url_for
from flask_login import login_required, logout_user


from app import login_manager, app
from .models import User


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(
        url_for('frontend.serve_pages', page='index')
    )
