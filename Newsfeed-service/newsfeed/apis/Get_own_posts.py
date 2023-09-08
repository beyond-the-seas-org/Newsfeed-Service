from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from newsfeed import db
from newsfeed import api

from newsfeed.models.post import *

from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError

@api.errorhandler(NoAuthorizationError)
def handle_auth_required(e):
    return {"message": "Authorization token is missing"}, 401


class Get_own_posts(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    @jwt_required()
    def get(self,user_id):

        try:
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

        except Exception as e:
            print({"message":"exception occured in get_own_posts"})
            print(e)
            return jsonify({"message":"exception occured in get_own_posts"})      



