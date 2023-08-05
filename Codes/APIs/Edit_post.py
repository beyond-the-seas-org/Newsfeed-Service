from flask import request,jsonify
from flask_restful import Resource
from sqlalchemy import func
from app import db



import sys
# append the path of the
# grand parent and parent directory
sys.path.append("....")
sys.path.append("..")

from Models.post import * 

 
#this class is for adding new post into database

class Edit_post(Resource):
    def post(self):
        post_id = request.json['post_id']
        edited_post_desc = request.json['post_desc']
        post = PostModel.query.get(post_id)
        post.post_desc = edited_post_desc  # Modify the attribute value
        db.session.commit()  # Commit the changes to the database
        return jsonify(post.json())
