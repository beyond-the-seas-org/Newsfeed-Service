from flask import request,jsonify
from flask_restful import Resource
from sqlalchemy import func
from app import db



import sys
# append the path of the
# grand parent and parent directory
sys.path.append("....")
sys.path.append("..")

from Models.comment import * 

 
#this class is for adding new post into database

class Edit_comment(Resource):
    def post(self):
        comment_id = request.json['comment_id']
        edited_comment = request.json['comment']
        comment = CommentModel.query.get(comment_id)
        comment.comment = edited_comment  # Modify the attribute value
        db.session.commit()  # Commit the changes to the database
        return jsonify(comment.json())
