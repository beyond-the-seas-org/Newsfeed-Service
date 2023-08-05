from flask import request,jsonify
from flask_restful import Resource
from sqlalchemy import func
from itertools import groupby

from app import db


import sys
# append the path of the
# grand parent and parent directory
sys.path.append("....")
sys.path.append("..")


from Models.post import * 


class Get_own_posts(Resource):
    def get(self,user_id):
        #db.aliased() is used to cross join two same table.."aliased_Student_model" is a different instance of StudentModel
        # aliased_Student_model = db.aliased(StudentModel)
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



