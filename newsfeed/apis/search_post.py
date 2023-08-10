from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from newsfeed import db
from newsfeed import api

from newsfeed.models.post import * 
from newsfeed.models.upvote import * 
from newsfeed.models.downvote import * 

class Search_Post(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self,current_user_id):
        try:
            tag = request.json['tag']

            all_posts = PostModel.query.order_by(PostModel.date.desc()).all()
            
            post_dicts=[]

            for post in all_posts:

                post_dict={}
                
                if tag.lower() in post.post_desc.lower(): #here lower() is used to ensure case insensitive search
                    post_dict['post_id'] = post.id
                    post_dict['user_id'] = post.profile_id
                    post_dict['post_desc']=post.post_desc
                    post_dict['date'] = post.date
                    post_dict['upvote']=post.upvotes
                    post_dict['downvotes']=post.downvotes
                    post_dict['upvote_status'] = False       
                    post_dict['downvote_status'] = False       

                    #Updating upvote and downvote status after each time loading the newsfeed
                    upvote_obj = UpvoteModel.query.filter_by(post_id=post['id'],profile_id=current_user_id).first() 
                    if upvote_obj:
                        post_dict['upvote_status'] = True       
                    downvote_obj = DownvoteModel.query.filter_by(post_id=post['id'],profile_id=current_user_id).first() 
                    if downvote_obj:
                        post_dict['downvote_status'] = True

                    post_dicts.append(post_dict)

            return jsonify(post_dicts)      
        except Exception as e:
            print({"message":"exception occured in search_post"})
            return jsonify({"message":"exception occured in search_post"})      

 



