from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from newsfeed import db
from newsfeed import api
import datetime

from newsfeed.models.post import * 
from newsfeed.models.community import *
from newsfeed.models.student import *
#this class is for adding new post into database

class Add_post(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            #for getting the next "id" for next entry of the "post" table
            max_id = db.session.query(func.max(PostModel.id)).scalar()
            if max_id:
                max_id = max_id + 1
            else:
                max_id = 1

            new_post = PostModel()
            new_post.id = max_id
            new_post.post_desc = request.json['post_desc']
            new_post.date = datetime.datetime.now()
            new_post.profile_id = request.json['user_id']
            new_post.community_id = None
            new_post.type = request.json['type']
            new_post.upvotes = 0
            new_post.downvotes = 0

            db.session.add(new_post)
            db.session.commit()


            return jsonify(new_post.json())
        except Exception as e:
            print({"message":"exception occured in add_post"})
            return jsonify({"message":"exception occured in add_post"})
