from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from newsfeed import db
from newsfeed import api

from newsfeed.models.post import * 

class Get_own_posts(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def get(self,user_id):
        all__own_posts =PostModel.query.filter_by(profile_id=user_id).order_by(PostModel.date.desc()).all()
       
        post_dicts=[]

        for post in all__own_posts:
            
            post_dict={}

            post_dict['post_id'] = post.id
            post_dict['post_desc']=post.post_desc
            post_dict['date'] = post.date
            post_dict['upvote']=post.upvotes
            post_dict['downvotes']=post.downvotes

            post_dicts.append(post_dict)

        return jsonify(post_dicts)       



