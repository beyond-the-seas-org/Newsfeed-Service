from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from newsfeed import db
from newsfeed import api
import pandas as pd
import requests

from newsfeed.models.comment import * 
from newsfeed.models.upvote import * 
from newsfeed.models.downvote import * 

class Get_Comment_of_a_post(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def get(self,current_user_id,post_id):

        try: 
            all_comments_of_a_post = CommentModel.query.filter_by(post_id=post_id).all()
            if len(all_comments_of_a_post) == 0 :  #if there is no comment of the post
                return jsonify([])

            all_comments_of_a_post_dicts = []
            for comment in all_comments_of_a_post:
                all_comments_of_a_post_dicts.append({"id":comment.id,"comment":comment.comment,"date":comment.date,"profile_id":comment.profile_id,"upvotes":comment.upvotes,"downvotes":comment.downvotes})

            #this is the panda tables of all comments    

            all_comments_of_a_post_pd = pd.DataFrame(all_comments_of_a_post_dicts)   
        
            #getting only "stduent_ids" from the "comment" table where post_id = post id

            all_student_ids = CommentModel.query.filter_by(post_id=post_id).with_entities(CommentModel.profile_id).order_by(CommentModel.date.desc()).all()
            #to send the "all_student_ids" to other service via a api call we have to convert it into a json format
            #eg. if all_student_ids = [1,2,3] then we have to send all_student_ids_json = [{"id":1},{"id":2},{"id":3}]
            all_student_ids_dicts = []
            for student_id in all_student_ids:
                all_student_ids_dicts.append({"student_id":student_id.profile_id})

            response = requests.post('http://localhost:5001//api/profile/get_student_names_and_images',json= all_student_ids_dicts)
        

            #from "response" we will buld a panda table of which has the mapping of the student ids with student names
            student_id_with_names_pd = pd.DataFrame(response.json())
            
            #now we will join those two panda tables
            final_pd = pd.merge(all_comments_of_a_post_pd, student_id_with_names_pd, left_on='profile_id', right_on='student_id')
            final_pd.drop_duplicates(inplace=True)
            #to show the recent comments at top
            final_pd = final_pd.sort_values(by='date', ascending=False)


            final_pd_dicts = final_pd.to_dict(orient='records')

            #Now we will form the json array which we will return to backend as a response
            comment_dicts=[]
        
            for comment in final_pd_dicts:
                
                comment_dict={}
                comment_dict['comment_id'] = comment['id']
                comment_dict['user_id'] = comment['profile_id']
                comment_dict['commentor'] = comment["username"]
                comment_dict['comment']= comment['comment']
                comment_dict['date']= comment['date']
                comment_dict['upvote']= comment['upvotes']
                comment_dict['downvotes']= comment['downvotes']
                comment_dict['upvote_status'] = False       
                comment_dict['downvote_status'] = False       


                #Updating upvote and downvote status after each time loading the newsfeed
                upvote_obj = UpvoteModel.query.filter_by(comment_id=comment['id'],profile_id=current_user_id).first() 
                if upvote_obj:
                    comment_dict['upvote_status'] = True       
                downvote_obj = DownvoteModel.query.filter_by(comment_id=comment['id'],profile_id=current_user_id).first() 
                if downvote_obj:
                    comment_dict['downvote_status'] = True

                comment_dicts.append(comment_dict)    

            return jsonify(comment_dicts)  
        
        except Exception as e:
            print({"message":"exception occured in get_comment_of_a_post"})
            print(e)
            return jsonify({"message":"exception occured in get_comment_of_a_post"})




