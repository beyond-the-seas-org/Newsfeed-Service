from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from newsfeed import db
from newsfeed import api
import datetime

from newsfeed.models.comment import * 
from newsfeed.models.student import * 

#this class is for adding new comment into database
class Add_comment(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:
            #for getting the next "id" for next entry of the "post" table

            new_comment = CommentModel()
            #new_comment.id = max_id
            new_comment.comment = request.json['comment']
            new_comment.date = datetime.datetime.now()
            new_comment.profile_id = request.json['user_id']
            new_comment.post_id = request.json['post_id']
            new_comment.upvotes = 0
            new_comment.downvotes = 0

            db.session.add(new_comment)
            db.session.commit()
            

            return jsonify(new_comment.json())

        except Exception as e:
            print({"message":"exception occured in add_comment"})
            return jsonify({"message":"exception occured in add_comment"})

        
        
        


        
