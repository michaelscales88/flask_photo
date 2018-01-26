from .server import app, db, init_db, BaseModel


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


# @app.route('/')
# def index():
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post action="/image" enctype=multipart/form-data>
#       <p><input type=file name=file>
#          <input type=submit value=Upload>
#     </form>
#     '''
