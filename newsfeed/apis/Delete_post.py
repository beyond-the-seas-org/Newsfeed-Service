from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from newsfeed import db
from newsfeed import api


from newsfeed.models.post import * 

#this class is for adding new post into database

class Delete_post(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):
        post_id = request.json['post_id']
        post = PostModel.query.get(post_id)
        if post is not None:
            db.session.delete(post)
            db.session.commit()  # Commit the changes to the database
            return jsonify({"message":"post has been deleted successfully"})
        else:
            return jsonify({"message":"error in Delete_post"})
