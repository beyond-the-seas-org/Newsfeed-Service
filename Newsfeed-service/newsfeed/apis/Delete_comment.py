from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from newsfeed import db
from newsfeed import api


from newsfeed.models.comment import * 

#this class is for adding new post into database

class Delete_comment(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

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
