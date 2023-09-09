from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from itertools import groupby
from newsfeed import db
from newsfeed import api
import pandas as pd
import requests
from newsfeed.models.post import * 
from newsfeed.models.upvote import * 
from newsfeed.models.downvote import * 

from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError

@api.errorhandler(NoAuthorizationError)
def handle_auth_required(e):
    return {"message": "Authorization token is missing"}, 401

class Get_all_post(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    
    @jwt_required()
    def get(self,current_user_id):
        # all_posts = db.session.query(StudentModel,PostModel).filter(StudentModel.id == PostModel.profile_id).order_by(PostModel.date.desc()).all()

        try:
            all_posts = PostModel.query.all()

            all_posts_dicts = []
            for post in all_posts:
                all_posts_dicts.append({"id":post.id,"post_desc":post.post_desc,"date":post.date,"profile_id":post.profile_id,"upvotes":post.upvotes,"downvotes":post.downvotes,"post_image":post.post_image})

            #this is the panda tables of all posts    
            all_posts_pd = pd.DataFrame(all_posts_dicts)   
            
            #getting only "stduent_ids" from the "post" table where post_id = post id
            all_student_ids = PostModel.query.with_entities(PostModel.profile_id).order_by(PostModel.date.desc()).all()
            #to send the "all_student_ids" to other service via a api call we have to convert it into a json format
            #eg. if all_student_ids = [1,2,3] then we have to send all_student_ids_json = [{"id":1},{"id":2},{"id":3}]
            all_student_ids_dicts = []
            for student_id in all_student_ids:
                all_student_ids_dicts.append({"student_id":student_id.profile_id})

            response = requests.post('http://localhost:5001//api/profile/get_student_names_and_images',json= all_student_ids_dicts)

            #from "response" we will buld a panda table of which has the mapping of the student ids with student names
            student_id_with_names_pd = pd.DataFrame(response.json())

            #now we will join those two panda tables
            final_pd = pd.merge(all_posts_pd, student_id_with_names_pd, left_on='profile_id', right_on='student_id')
            final_pd.drop_duplicates(inplace=True)

            #to show the recent comments at top
            final_pd = final_pd.sort_values(by='date', ascending=False)
            final_pd_dicts = final_pd.to_dict(orient='records')

            #NOw we will form the json array which we will return to backend as a response
            post_dicts=[]

            for post in final_pd_dicts:
            
                post_dict={}
                post_dict['user_id'] = post['profile_id']
                post_dict['user_name'] = post['username']
                post_dict['profile_picture_link'] = post['profile_picture_link']
                post_dict['post_id'] = post['id']
                post_dict['date'] = post['date']
                post_dict['post_desc']=post['post_desc']
                post_dict['upvotes']=post['upvotes']
                post_dict['downvotes']=post['downvotes']
                post_dict['post_image']=post['post_image']
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
            print({"message":"exception occured in get_posts"})
            print(e)
            return jsonify({"message":"exception occured in get_posts"})      


            







