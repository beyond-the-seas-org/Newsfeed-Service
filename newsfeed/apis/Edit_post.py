from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from newsfeed import db
from newsfeed import api

from newsfeed.models.post import * 
 
#this class is for adding new post into database
class Edit_post(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def put(self):
        post_id = request.json['post_id']
        edited_post_desc = request.json['post_desc']
        post = PostModel.query.get(post_id)
        post.post_desc = edited_post_desc  # Modify the attribute value
        db.session.commit()  # Commit the changes to the database
        return jsonify(post.json())
