from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from newsfeed import db
from newsfeed import api


from newsfeed.models.comment import * 

from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError

@api.errorhandler(NoAuthorizationError)
def handle_auth_required(e):
    return {"message": "Authorization token is missing"}, 401

#this class is for adding new post into database

class Delete_comment(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    @jwt_required()
    def put(self):

        try:
            comment_id = request.json['comment_id']
            comment = CommentModel.query.get(comment_id)
            if comment is not None:
                db.session.delete(comment)
                db.session.commit()  # Commit the changes to the database
                return jsonify({"message":"comment has been deleted successfully"})
            else:
                return jsonify({"message":"The comment does not exist"})
        except Exception as e:
            print({"message":"exception occured in delete_comment"})
            print(e)
            return jsonify({"message":"exception occured in delete_comment"})
