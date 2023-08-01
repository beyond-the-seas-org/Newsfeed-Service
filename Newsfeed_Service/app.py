from flask import Flask,request,jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import func
from itertools import groupby

import datetime
import sys



import os
import psycopg2
from dotenv import load_dotenv

app = Flask(__name__)
api = Api(app)

# Load environment variables
load_dotenv()
db_url = os.getenv('DATABASE_URL')

# Connect to database
conn = psycopg2.connect(db_url, sslmode='prefer')

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import models
 
# append the path of the
# parent directory
sys.path.append("..") #this is needed to import file from sibling directory

from Database_Service.models import * 
from Database_Service.models.student import *
from Database_Service.models.project import *
from Database_Service.models.field import * 
from Database_Service.models.publication import * 
from Database_Service.models.post import * 
from Database_Service.models.comment import * 
from Database_Service.models.community import * 



migrate = Migrate(app, db)

class Greet(Resource):
    def get(self):
        return {'message':'Hello World'}
        
api.add_resource(Greet,'/hello')




#this class is for adding a student obejct(i.e adding a row) in "student table"
class Create_profile(Resource):
    def post(self):
        new_student = StudentModel()

        #for getting the next "id" for next entry of the "post" table
        max_id = db.session.query(func.max(StudentModel.id)).scalar()
        if (max_id == 'None'):
            max_id = 1
        else:
            max_id = max_id + 1

        new_student.id = max_id
        new_student.username = request.json['username']
        new_student.first_name= request.json['first_name']
        new_student.last_name = request.json['last_name']
        new_student.primary_email = request.json['primary_email']
        new_student.gender = request.json['gender']
        new_student.age = request.json['age']
        new_student.secondary_email = request.json['secondary_email']
        new_student.bsc_year_of_passing  = request.json['bsc_year_of_passing']
        new_student.ms_year_of_passing = request.json['ms_year_of_passing']
        new_student.bsc_cgpa = request.json['bsc_cgpa']
        new_student.ms_cgpa = request.json['bsc_cgpa']
        new_student.bsc_university = request.json['bsc_university']
        new_student.ms_university = request.json['ms_university']
        new_student.github_link = request.json['github_link']
        new_student.linkedin_link = request.json['linkedin_link']
        new_student.current_address = request.json['current_address']
        new_student.website_link = request.json['website_link']
        new_student.gre_verbal_quant_score = request.json['gre_verbal_quant_score']
        new_student.gre_awa_score = request.json['gre_awa_score']
        new_student.toefl_score = request.json['toefl_score']
        new_student.ielts_score = request.json['ielts_score']


        db.session.add(new_student)
        db.session.commit()

        #print(new_student.json())
        return jsonify(new_student.json())

api.add_resource(Create_profile,'/create_profile')


#this class is for adding new post into database

class Add_post(Resource):
    def post(self):


        #for getting the next "id" for next entry of the "post" table
        max_id = db.session.query(func.max(PostModel.id)).scalar()
        if (max_id == 'None'):
            max_id = 1
        else:
            max_id = max_id + 1


        
        new_post = PostModel()
        new_post.id = max_id
        new_post.post_desc = request.json['post_desc']
        
        Datetime = request.json['date']

        """here the "Datetime" will contain a string like "2023-07-31 15:30:00"
        so , we have to convert this "Datetime" string into a "datetime" type object before entering datetime into database
        So, to convert into "datetime" object we have to call "datetime.datetime(2023,07,31,15,30,0)" and this will return a "datetime object..Thats why the following split() is performed"""

        Datetime = Datetime.split(' ')
        date = Datetime[0].split("-")
        time = Datetime[1].split(":")

        Datetime = datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(time[0]),int(time[1]),int(time[2]))
        new_post.date = Datetime

        new_post.profile_id = request.json['user_id']
        new_post.community_id = None
        new_post.type = request.json['type']
        new_post.upvotes = 0
        new_post.downvotes = 0

        db.session.add(new_post)
        db.session.commit()


        return jsonify(new_post.json())

api.add_resource(Add_post,'/add_post')

#this class is for getting recent posts from database


class Get_all_post(Resource):
    def get(self):
        #db.aliased() is used to cross join two same table.."aliased_Student_model" is a different instance of StudentModel
        aliased_Student_model = db.aliased(StudentModel)
        all_posts = db.session.query(StudentModel,PostModel,CommentModel,aliased_Student_model).filter(StudentModel.id == PostModel.profile_id).filter(CommentModel.post_id == PostModel.id).filter(CommentModel.profile_id == aliased_Student_model.id).order_by(PostModel.date.desc()).all()

        """
        Here the logic is little bit tricky..here after the above query a list of tuples will be retrieved.each tuple represents a 
        row of joined table..A single tuple will look like below..
        
        (student1,post1,comment2,student2) 
        ==> this tuple means student1/user1 did a post named "post1" and there is a comment for this post named "comment2" and the comment was done by "student2"

        So,the retrieved list of tuples after the above query will look like this 
        [(student1,post1,comment2,student2),
         (student2,post2,comment1,student1),
         (student3,post3,comment3,student1),
         (student3,post3,comment4,student2),.....  ]

         Now we got the above tuples where we can see both post1 has post2 has single comment but post 3 has two comments..But we want to return a list of post as a response to the frontend..That means we want to return a list of json/dictionary where each json/dictionary will correspond to a single post..For example for the above list of tuple we want to return something like this,
         [
            {
                "post_id" : post1
                "user_id" : student1
                "comments" :["comment2" posted by "student2"] 
            },
            {
                "post_id" : post2
                "user_id" : student2
                "comments" :["comment1" posted by "student1"] 
            },
            {
                "post_id" : post2
                "user_id" : student2
                "comments" :["comment3" posted by "student1" , "comment4" posted by "student2"  ] 
            },
                   
         ] 

         So, to return this type of list of json we need to group by the above list of tuples(which we got from query) according to 1st and 2nd element of each tuple(1st element=student who posts(eg.student1),2nd element = the post(eg. post1) )

        
        """

        # Group the "all_posts" by the 1st and 2nd element of each tuple(i.e ,1st element=student who posts,2nd element = the post )
        grouped_tuples = {}
        #x[0] means 1st element of tuple and x[1] means  2nd element of tuple
        for key, group in groupby(all_posts, key=lambda x: (x[0],x[1])): 
            grouped_tuples[key] = list(group)

       # print(grouped_tuples)

        post_dicts=[]

        for key in grouped_tuples:
            
            post_dict={}
            student = key[0]
            post = key[1]
            comments_and_commentors = grouped_tuples[key]

            post_dict['user_id'] = student.id
            post_dict['user_name'] = student.username
            post_dict['post_id'] = post.id
            post_dict['post_desc']=post.post_desc
            post_dict['upvote']=post.upvotes
            post_dict['downvotes']=post.downvotes

            all_comments=[]
            for comment_and_commentor in comments_and_commentors:
                comment_details={}
                comment = comment_and_commentor[2]
                commentor = comment_and_commentor[3]
                comment_details['comment'] = comment.comment
                comment_details['commentor'] = commentor.username
                all_comments.append(comment_details)

            post_dict['comments'] = all_comments    





            post_dicts.append(post_dict)

        return jsonify(post_dicts)  




api.add_resource(Get_all_post,'/get_posts')

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

        


api.add_resource(Add_comment,'/add_comment')

#this method is for upvote or downvote for post

class Upvote_or_Downvote_for_post(Resource):
    def post(self,vote):
        post_id = request.json['post_id']
        post = PostModel.query.get(post_id)

        if (vote == "upvote"):  
            if post: #if post is not none
                post.upvotes = post.upvotes + 1  # Modify the attribute value
                db.session.commit()  # Commit the changes to the database
                return jsonify(post.json())
            else:
                return jsonify({"message:error in upvote_or_downvote"})  
         
        if (vote == "downvote"):  
          
            if post: #if post is not none
                post.downvotes = post.downvotes + 1  # Modify the attribute value
                db.session.commit()  # Commit the changes to the database
                return jsonify(post.json())

            else:
                return jsonify({"message:error in upvote_or_downvote"})  





api.add_resource(Upvote_or_Downvote_for_post,'/post/<vote>')


#this method is for upvote or downvote for comment

class Upvote_or_Downvote_for_comment(Resource):
    def post(self,vote):
        comment_id = request.json['comment_id']
        comment = CommentModel.query.get(comment_id)

        if (vote == "upvote"):  
            if comment: #if post is not none
                comment.upvotes = comment.upvotes + 1  # Modify the attribute value
                db.session.commit()  # Commit the changes to the database
                return jsonify(comment.json())
            else:
                return jsonify({"message:error in upvote_or_downvote"})  
         
        if (vote == "downvote"):  
          
            if comment: #if post is not none
                comment.downvotes = comment.downvotes + 1  # Modify the attribute value
                db.session.commit()  # Commit the changes to the database
                return jsonify(comment.json())

            else:
                return jsonify({"message:error in upvote_or_downvote"})  





api.add_resource(Upvote_or_Downvote_for_comment,'/comment/<vote>')




if __name__ == '__main__':
    app.run(port=5000, debug=True)



