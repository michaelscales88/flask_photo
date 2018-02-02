import os
from flask import jsonify, current_app
from flask_restful import Resource, reqparse
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from .models import Image
from .utilities import allowed_file, ImageSchema, send_or_404


class ImagesAPI(Resource):

    def __init__(self):
        self.schema = ImageSchema(many=True)
        parser = reqparse.RequestParser()
        parser.add_argument('image')
        self.args = parser.parse_args()
        super().__init__()

    def get(self):
        images = 'pic.jpg'
        if self.args['image']:
            print('getting', self.args['image'])
        else:
            results = Image.query.filter(Image.visible == True).all()
            # print(results)
            images = self.schema.dump(results).data
            print(images)
            print('getting all images')
        return jsonify(
            data=images
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
        print('hit GET ImageAPI')
        return send_or_404(self.args['image'])

    def post(self):
        print('Hit PUT ImageAPI')
        # Check whether the request contains a file
        if (
                self.args['file'] and
                self.args['file'].filename and
                allowed_file(self.args['file'].filename)
        ):
            # Save the image to the upload folder
            file_name = secure_filename(self.args['file'].filename)
            self.args['file'].save(
                os.path.join(current_app.config['UPLOAD_FOLDER'], file_name)
            )
            # Create record for the image
            Image.create(
                title=self.args['file'].filename,
                description='',
                filename=self.args['file'].filename
            )
            print('adding an image')

    def delete(self):
        print('Hit DELETE ImageAPI')
        pass
