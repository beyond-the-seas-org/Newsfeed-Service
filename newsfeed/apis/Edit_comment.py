from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from newsfeed import db
from newsfeed import api

from newsfeed.models.comment import * 

 
#this class is for adding new post into database

class Edit_comment(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def put(self):
        comment_id = request.json['comment_id']
        edited_comment = request.json['comment']
        comment = CommentModel.query.get(comment_id)
        comment.comment = edited_comment  # Modify the attribute value
        db.session.commit()  # Commit the changes to the database
        return jsonify(comment.json())
