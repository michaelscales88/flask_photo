from flask import jsonify
from flask_restful import Resource, reqparse
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from .models import Image
from .utilities import allowed_file, ImageSchema, send_or_404, save_file


class ImagesAPI(Resource):

    def __init__(self):
        self.schema = ImageSchema(many=True)
        parser = reqparse.RequestParser()
        parser.add_argument('image')
        self.args = parser.parse_args()
        super().__init__()

    def get(self):
        results = Image.query.filter(Image.visible == True).all()
        print(results)
        return jsonify(
            data=self.schema.dump(results).data
        )


class ImageAPI(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('image')
        parser.add_argument('file', type=FileStorage, location='files')
        self.args = parser.parse_args()
        super().__init__()

    def __del__(self):
        Image.session.commit()

    def get(self):
        print('sending', self.args['image'])
        return send_or_404(self.args['image'])

    def post(self):
        # Check whether the request contains a file
        if (
            self.args['file'] and
            self.args['file'].filename and
            allowed_file(self.args['file'].filename)
        ):
            # Save the image to the upload folder
            successful_save = save_file(
                self.args['file'],
                secure_filename(self.args['file'].filename)
            )

            # Create record for the image
            if successful_save:
                Image.create(
                    title=self.args['file'].filename,
                    description='',
                    filename=self.args['file'].filename
                )

    def delete(self):
        print('Hit DELETE ImageAPI')
        pass
