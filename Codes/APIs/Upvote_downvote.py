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
from Models.comment import * 



#this method is for upvote or downvote for post

class Upvote_or_Downvote_for_post(Resource):
    def post(self,vote):
        post_id = request.json['post_id']
        post = PostModel.query.get(post_id)

        if (vote == "upvote"):  
            if post: #if post is not none
                post.upvotes = post.upvotes + 1  # Modify the attribute value
                db.session.commit()  # Commit the changes to the database
                return jsonify(post.json())
            else:
                return jsonify({"message:error in upvote_or_downvote"})  
         
        if (vote == "downvote"):  
          
            if post: #if post is not none
                post.downvotes = post.downvotes + 1  # Modify the attribute value
                db.session.commit()  # Commit the changes to the database
                return jsonify(post.json())

            else:
                return jsonify({"message:error in upvote_or_downvote"})  




#this method is for upvote or downvote for comment

class Upvote_or_Downvote_for_comment(Resource):
    def post(self,vote):
        comment_id = request.json['comment_id']
        comment = CommentModel.query.get(comment_id)

        if (vote == "upvote"):  
            if comment: #if post is not none
                comment.upvotes = comment.upvotes + 1  # Modify the attribute value
                db.session.commit()  # Commit the changes to the database
                return jsonify(comment.json())
            else:
                return jsonify({"message:error in upvote_or_downvote"})  
         
        if (vote == "downvote"):  
          
            if comment: #if post is not none
                comment.downvotes = comment.downvotes + 1  # Modify the attribute value
                db.session.commit()  # Commit the changes to the database
                return jsonify(comment.json())

            else:
                return jsonify({"message:error in upvote_or_downvote"})  





