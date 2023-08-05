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

class Delete_post(Resource):
    def post(self):
        post_id = request.json['post_id']
        post = PostModel.query.get(post_id)
        if post is not None:
            db.session.delete(post)
            db.session.commit()  # Commit the changes to the database
            return jsonify({"message":"post has been deleted successfully"})
        else:
            return jsonify({"message":"error in Delete_post"})
