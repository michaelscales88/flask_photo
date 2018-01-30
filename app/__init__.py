from flask import url_for
from flask_bootstrap import Bootstrap
from .server import app, db, login_manager, ma, init_db, BaseModel
from .services import init_nav


Bootstrap(app)
init_nav(app)

from .frontend import api_bp as frontend_bp
from .backend import api_bp as backend_bp

app.register_blueprint(frontend_bp)
app.register_blueprint(backend_bp)


# Configuration for APP
@app.before_first_request
def startup_setup():
    # Make database and tables
    init_db()

    # Inject session to be used by Models
    BaseModel.set_session(db.session)

    # Ensure the photo directory exists
    import os
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    login_manager.login_view = url_for('frontend.serve_pages', page='login')
