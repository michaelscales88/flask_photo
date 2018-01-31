from flask import url_for, g
from flask_bootstrap import Bootstrap
from flask_login import current_user


from .server import app, db, login_manager, ma, init_db, BaseModel
from .services import init_nav, make_dir


Bootstrap(app)
init_nav(app)

from .frontend import api_bp as frontend_bp
from .backend import api_bp as backend_bp

app.register_blueprint(frontend_bp)
app.register_blueprint(backend_bp)


# Configuration for APP
@app.before_first_request
def startup_setup():
    # Ensure the tmp/images directory exists
    make_dir(app.config['UPLOAD_FOLDER'])

    # Make database and tables
    init_db()

    # Inject session to be used by Models
    BaseModel.set_session(db.session)

    login_manager.login_view = url_for('frontend.serve_pages', page='login')


@app.before_request
def before_request():
    g.user = current_user
