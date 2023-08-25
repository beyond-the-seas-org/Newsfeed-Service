from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from newsfeed import db
from newsfeed import api

from newsfeed.models.post import * 

"""this API will return all the research posts to the "Chatbot-Service"(we assume that all the funting posts at our platform
will start as "#funding_post"  """
class Get_research_posts(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def get(self):

        try:
            all_research_posts =PostModel.query.filter(PostModel.post_desc.startswith("#research_post")).order_by(PostModel.date.desc()).all()
        
            post_dicts=[]

            for post in all_research_posts:
                
                post_dict={}

                post_dict['post_id'] = post.id
                post_dict['post_desc']=post.post_desc
                post_dict['date'] = post.date

                post_dicts.append(post_dict)

            return jsonify(post_dicts) 

        except Exception as e:
            print({"message":"exception occured in get_research_posts"})
            print(e)
            return jsonify({"message":"exception occured in get_research_posts"})      



