from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from newsfeed import db
from newsfeed import api

from newsfeed.models.student import *
from newsfeed.models.comment import * 

class Get_Comment_of_a_post(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def get(self,post_id):
        #db.aliased() is used to cross join two same table.."aliased_Student_model" is a different instance of StudentModel
        # aliased_Student_model = db.aliased(StudentModel)
        all_comments_of_a_post = db.session.query(StudentModel,CommentModel).filter(StudentModel.id == CommentModel.profile_id).filter(CommentModel.post_id == post_id).order_by(CommentModel.date.desc()).all()
    
        comment_dicts=[]

        for student,comment in all_comments_of_a_post:
            
            comment_dict={}
            comment_dict['comment_id'] = comment.id
            comment_dict['commentor'] = student.username
            comment_dict['comment']=comment.comment
            comment_dict['upvote']=comment.upvotes
            comment_dict['downvotes']=comment.downvotes
            comment_dicts.append(comment_dict)

        return jsonify(comment_dicts)  



