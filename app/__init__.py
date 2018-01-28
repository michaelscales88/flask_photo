from flask_bootstrap import Bootstrap
from .server import app, db, init_db, BaseModel


Bootstrap(app)
init_db()

from .frontend import api_bp as frontend_bp
from .backend import api_bp as backend_bp

app.register_blueprint(frontend_bp)
app.register_blueprint(backend_bp)


# Configuration for APP
@app.before_first_request
def startup_setup():
    # Inject session to be used by Models
    BaseModel.set_session(db.session)

    # Ensure the photo directory exists
    import os
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
