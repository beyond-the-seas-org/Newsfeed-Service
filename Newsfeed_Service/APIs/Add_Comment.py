from flask import request,jsonify
from flask_restful import Resource
from sqlalchemy import func
from app import db
import datetime



import sys
# append the path of the
# grand parent and parent directory
sys.path.append("....")
sys.path.append("..")


from Database_Service.models.comment import * 


#this class is for adding new comment into database
class Add_comment(Resource):
    def post(self):

        #for getting the next "id" for next entry of the "post" table
        max_id = db.session.query(func.max(CommentModel.id)).scalar()
        if (max_id == 'None'):
            max_id = 1
        else:
            max_id = max_id + 1


        new_comment = CommentModel()
        
        new_comment.id = max_id
        new_comment.comment = request.json['comment']
        Datetime = request.json['date']

        """
        here the "Datetime" will contain a string like "2023-07-31 15:30:00"
        so , we have to convert this "Datetime" string into a "datetime" type object before entering datetime into database
        So, to convert into "datetime" object we have to call "datetime.datetime(2023,07,31,15,30,0)" and this will return a datetime object..Thats why the following split() is performed
        """

        Datetime = Datetime.split(' ')
        date = Datetime[0].split("-")
        time = Datetime[1].split(":")

        Datetime = datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(time[0]),int(time[1]),int(time[2]))
        new_comment.date = Datetime

        new_comment.profile_id = request.json['user_id']
        new_comment.post_id = request.json['post_id']

        new_comment.upvotes = 0
        new_comment.downvotes = 0

        db.session.add(new_comment)
        db.session.commit()

        return jsonify(new_comment.json())

        
