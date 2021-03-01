from main import app, api, ns
from flask_restplus import Resource
from flask import request, Blueprint
import json

gbRobot = Blueprint('gbRobot', __name__)


@ns.route('/')
class CategoryCollection(Resource):

    def get(self):
        model = {
            'model': 'get'
        }
        return json.dumps(model)

    @api.response(201, 'Category successfully created.')
    def post(self):
        """Creates a new blog category."""
        model = {
            'model': 'post'
        }
        return json.dumps(model)


"""
@ns.route('/<int:id>')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):

    def get(self, id):
        
        return get_category(id)

    @api.response(204, 'Category successfully updated.')
    def put(self, id):
        
        update_category(id, request.json)
        return None, 204

    @api.response(204, 'Category successfully deleted.')
    def delete(self, id):
        
        delete_category(id)
        return None, 204
"""