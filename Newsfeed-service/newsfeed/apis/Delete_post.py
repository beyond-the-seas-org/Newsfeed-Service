from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from newsfeed import db
from newsfeed import api


from newsfeed.models.post import * 

#this class is for adding new post into database

from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError

@api.errorhandler(NoAuthorizationError)
def handle_auth_required(e):
    return {"message": "Authorization token is missing"}, 401


class Delete_post(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    @jwt_required()
    def put(self):

        try:
            post_id = request.json['post_id']
            post = PostModel.query.get(post_id)
            if post is not None:
                db.session.delete(post)
                db.session.commit()  # Commit the changes to the database
                return jsonify({"message":"post has been deleted successfully"})
            else:
                return jsonify({"message":"The post does not exist"})
        except Exception as e:
            print({"message":"exception occured in delete_post"})
            print(e)
            return jsonify({"message":"exception occured in delete_post"})
