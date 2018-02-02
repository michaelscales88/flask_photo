# user/utilities.py
from flask import redirect, url_for, request, flash, abort, render_template, g
from flask_login import login_required, logout_user, login_user
from urllib.parse import urlparse, urljoin


from app import login_manager, app
from .forms import LoginForm
from .models import User


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return (
        test_url.scheme in ('http', 'https')
        and ref_url.netloc == test_url.netloc
    )


def get_redirect_target():
    for target in request.values.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return target
        else:
            return abort(400)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/login-user', methods=["POST"])
def login():

    next = get_redirect_target()
    form = LoginForm()

    if request.method == 'POST':
        if g.user and g.user.is_authenticated:
            pass
        elif form.validate_on_submit():
            email = form.login.data
            password = form.password.data
            remember = form.remember_me.data
            user = User.query.filter(User.email == email).first()

            if user and user.password == password:
                success = login_user(user, remember=remember)
                flash('Login {s}.'.format(s='success!' if success else 'failed!'))

                if next == url_for('frontend.serve_pages', page='login') and success:
                    next = None

                if not success:
                    flash('Invalid username or password.')
            else:
                flash('Invalid username or password.')

            return redirect(next if next else url_for('frontend.serve_pages'))
    return render_template(
        'login.html',
        title='Sign In',
        next=next,
        form=form
    )


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(
        url_for('frontend.serve_pages', page='index')
    )
