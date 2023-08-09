from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from itertools import groupby
from newsfeed import db
from newsfeed import api
import pandas as pd
import requests

from newsfeed.models.post import * 


# #this class is for getting recent posts from database

# class Get_all_post(Resource):
#     def get(self):
#         #db.aliased() is used to cross join two same table.."aliased_Student_model" is a different instance of StudentModel
#         aliased_Student_model = db.aliased(StudentModel)
#         all_posts = db.session.query(StudentModel,PostModel,CommentModel,aliased_Student_model).filter(StudentModel.id == PostModel.profile_id).filter(CommentModel.post_id == PostModel.id).filter(CommentModel.profile_id == aliased_Student_model.id).order_by(PostModel.date.desc()).all()

#         """
#         Here the logic is little bit tricky..here after the above query a list of tuples will be retrieved.each tuple represents a 
#         row of joined table..A single tuple will look like below..
        
#         (student1,post1,comment2,student2) 
#         ==> this tuple means student1/user1 did a post named "post1" and there is a comment for this post named "comment2" and the comment was done by "student2"

#         So,the retrieved list of tuples after the above query will look like this 
#         [(student1,post1,comment2,student2),
#          (student2,post2,comment1,student1),
#          (student3,post3,comment3,student1),
#          (student3,post3,comment4,student2),.....  ]

#          Now we got the above tuples where we can see both post1 has post2 has single comment but post 3 has two comments..But we want to return a list of post as a response to the frontend..That means we want to return a list of json/dictionary where each json/dictionary will correspond to a single post..For example for the above list of tuple we want to return something like this,
#          [
#             {
#                 "post_id" : post1
#                 "user_id" : student1
#                 "comments" :["comment2" posted by "student2"] 
#             },
#             {
#                 "post_id" : post2
#                 "user_id" : student2
#                 "comments" :["comment1" posted by "student1"] 
#             },
#             {
#                 "post_id" : post2
#                 "user_id" : student2
#                 "comments" :["comment3" posted by "student1" , "comment4" posted by "student2"  ] 
#             },
                   
#          ] 

#          So, to return this type of list of json we need to group by the above list of tuples(which we got from query) according to 1st and 2nd element of each tuple(1st element=student who posts(eg.student1),2nd element = the post(eg. post1) )

        
#         """

#         # Group the "all_posts" by the 1st and 2nd element of each tuple(i.e ,1st element=student who posts,2nd element = the post )
#         grouped_tuples = {}
#         #x[0] means 1st element of tuple and x[1] means  2nd element of tuple
#         for key, group in groupby(all_posts, key=lambda x: (x[0],x[1])): 
#             grouped_tuples[key] = list(group)

#        # print(grouped_tuples)

#         post_dicts=[]

#         for key in grouped_tuples:
            
#             post_dict={}
#             student = key[0]
#             post = key[1]
#             comments_and_commentors = grouped_tuples[key]

#             post_dict['user_id'] = student.id
#             post_dict['user_name'] = student.username
#             post_dict['post_id'] = post.id
#             post_dict['post_desc']=post.post_desc
#             post_dict['upvote']=post.upvotes
#             post_dict['downvotes']=post.downvotes

#             all_comments=[]
#             for comment_and_commentor in comments_and_commentors:
#                 comment_details={}
#                 comment = comment_and_commentor[2]
#                 commentor = comment_and_commentor[3]
#                 comment_details['comment'] = comment.comment
#                 comment_details['commentor'] = commentor.username
#                 comment_details['upvotes'] = comment.upvotes
#                 comment_details['downvotes'] = comment.downvotes
                
#                 all_comments.append(comment_details)

#             post_dict['comments'] = all_comments    





#             post_dicts.append(post_dict)

#         return jsonify(post_dicts)  

class Get_all_post(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def get(self):
        # all_posts = db.session.query(StudentModel,PostModel).filter(StudentModel.id == PostModel.profile_id).order_by(PostModel.date.desc()).all()

        all_posts = PostModel.query.all()

        all_posts_dicts = []
        for post in all_posts:
            all_posts_dicts.append({"id":post.id,"post_desc":post.post_desc,"date":post.date,"profile_id":post.profile_id,"upvotes":post.upvotes,"downvotes":post.downvotes})

        #this is the panda tables of all posts    
        all_posts_pd = pd.DataFrame(all_posts_dicts)   
        
        #getting only "stduent_ids" from the "post" table where post_id = post id
        all_student_ids = PostModel.query.with_entities(PostModel.profile_id).order_by(PostModel.date.desc()).all()
        #to send the "all_student_ids" to other service via a api call we have to convert it into a json format
        #eg. if all_student_ids = [1,2,3] then we have to send all_student_ids_json = [{"id":1},{"id":2},{"id":3}]
        all_student_ids_dicts = []
        for student_id in all_student_ids:
            all_student_ids_dicts.append({"student_id":student_id.profile_id})

        response = requests.post('http://localhost:5001//api/profile/get_student_names',json= all_student_ids_dicts)
    

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
            post_dict['post_id'] = post['id']
            post_dict['date'] = post['date']
            post_dict['post_desc']=post['post_desc']
            post_dict['upvote']=post['upvotes']
            post_dict['downvotes']=post['downvotes']

            post_dicts.append(post_dict)

        return jsonify(post_dicts)  







