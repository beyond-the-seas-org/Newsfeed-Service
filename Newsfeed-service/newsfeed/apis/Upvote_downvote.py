from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from newsfeed import db
from newsfeed import api

from newsfeed.models.post import * 
from newsfeed.models.comment import * 
from newsfeed.models.upvote import * 
from newsfeed.models.downvote import * 
 

#this method is for upvote or downvote for post

class Upvote_or_Downvote_for_post(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def put(self,vote,i_or_d):

        try:

            post_id = request.json['post_id']
            profile_id = request.json['user_id']

            post = PostModel.query.get(post_id)

            if (vote == "upvote" and i_or_d =="increment" ):  
                if post: #if post is not none
                    post.upvotes = post.upvotes + 1  

                    #adding an into "upvote" table                    
                    new_upvote = UpvoteModel()
                    new_upvote.post_id = post_id
                    new_upvote.comment_id = None
                    new_upvote.type = 'post'
                    new_upvote.profile_id = profile_id

                    db.session.add(new_upvote)
                    db.session.commit()  # Commit the changes to the database
                    return jsonify(post.json())
                else:
                    return jsonify({"message:error in upvote_or_downvote"})  
                
            if (vote == "upvote" and i_or_d =="decrement" ):  
                if post: #if post is not none
                    post.upvotes = post.upvotes - 1  # Modify the attribute value
                    #upvotes and downvotes can not be less than 0
                    if(post.upvotes < 0):
                        post.upvotes = 0
                    #deleting the upvote entry from "upvote" table
                    target_upvote = UpvoteModel.query.filter_by(post_id=post_id,profile_id=profile_id).first()
                    if target_upvote:
                         db.session.delete(target_upvote)

                    db.session.commit()  # Commit the changes to the database
                    return jsonify(post.json())
                else:
                    return jsonify({"message:error in upvote_or_downvote"})  
            
            if (vote == "downvote" and i_or_d =="increment"):  
            
                if post: #if post is not none
                    post.downvotes = post.downvotes + 1  # Modify the attribute value

                    #adding an into "downvote" table                    
                    new_downvote = DownvoteModel()
                    new_downvote.post_id = post_id
                    new_downvote.comment_id = None
                    new_downvote.type = 'post'
                    new_downvote.profile_id = profile_id

                    db.session.add(new_downvote)
                    db.session.commit()  # Commit the changes to the database
                    return jsonify(post.json())

                else:
                    return jsonify({"message:error in upvote_or_downvote"})  
                
            if (vote == "downvote" and i_or_d =="decrement"):  
            
                if post: #if post is not none
                    post.downvotes = post.downvotes - 1  # Modify the attribute value

                    #upvotes and downvotes can not be less than 0
                    if(post.downvotes < 0):
                        post.downvotes = 0

                    #deleting the downvote entry from "downvote" table
                    target_downvote = DownvoteModel.query.filter_by(post_id=post_id,profile_id=profile_id).first()
                    if target_downvote:
                         db.session.delete(target_downvote)
                    db.session.commit()  # Commit the changes to the database
                    return jsonify(post.json())

                else:
                    return jsonify({"message:error in upvote_or_downvote"})


        except Exception as e:
            print({"message":"exception occured in post_upvote_downvote"})
            print(e)
            return jsonify({"message":"exception occured in post_upvote_downvote"})      
   




#this method is for upvote or downvote for comment

class Upvote_or_Downvote_for_comment(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def put(self,vote,i_or_d):

        try:
            comment_id = request.json['comment_id']
            profile_id = request.json['user_id']

            comment = CommentModel.query.get(comment_id)

            if (vote == "upvote" and i_or_d == "increment"):  
                if comment: #if post is not none
                    comment.upvotes = comment.upvotes + 1  # Modify the attribute value
                    
                    #adding an into "upvote" table                    
                    new_upvote = UpvoteModel()
                    new_upvote.comment_id = comment_id
                    new_upvote.post_id = None
                    new_upvote.type = 'comment'
                    new_upvote.profile_id = profile_id

                    db.session.add(new_upvote)
                    db.session.commit()  # Commit the changes to the database
                    return jsonify(comment.json())
                else:
                    return jsonify({"message:error in upvote_or_downvote"})  
                
            if (vote == "upvote" and i_or_d == "decrement"):  
                if comment: #if post is not none
                    #upvotes and downvotes can not be less than 0
                    comment.upvotes = comment.upvotes - 1  # Modify the attribute value
                    if(comment.upvotes < 0):
                        comment.upvotes = 0
                    #deleting the upvote entry from "upvote" table
                    target_upvote = UpvoteModel.query.filter_by(comment_id=comment_id,profile_id=profile_id).first()
                    if target_upvote:
                        db.session.delete(target_upvote)                    
                    db.session.commit()  # Commit the changes to the database

                    return jsonify(comment.json())
                else:
                    return jsonify({"message:error in upvote_or_downvote"})  
            
            if (vote == "downvote" and  i_or_d == "increment" ):  
            
                if comment: #if post is not none
                    comment.downvotes = comment.downvotes + 1  # Modify the attribute value
                  
                    #adding an into "downvote" table                    
                    new_downvote = DownvoteModel()
                    new_downvote.comment_id = comment_id
                    new_downvote.post_id = None
                    new_downvote.type = 'comment'
                    new_downvote.profile_id = profile_id

                    db.session.add(new_downvote)
                    db.session.commit()  # Commit the changes to the database
                    return jsonify(comment.json())

                else:
                    return jsonify({"message:error in upvote_or_downvote"})  
                
            if (vote == "downvote" and  i_or_d == "decrement" ):  
            
                if comment: #if post is not none
                    comment.downvotes = comment.downvotes - 1  # Modify the attribute value
                    
                    #upvotes and downvotes can not be less than 0
                    if(comment.downvotes < 0):
                        comment.downvotes = 0

                    #deleting the upvote entry from "upvote" table
                    target_downvote = DownvoteModel.query.filter_by(comment_id=comment_id,profile_id=profile_id).first()
                    if target_downvote:
                        db.session.delete(target_downvote) 

                    db.session.commit()  # Commit the changes to the database
                    return jsonify(comment.json())

                else:
                    return jsonify({"message:error in upvote_or_downvote"})  


        except Exception as e:
            print({"message":"exception occured in comment_upvote_downvote"})
            print(e)
            return jsonify({"message":"exception occured in comment_upvote_downvote"})      
   


