from APIs.Create_Profile import *
from APIs.Add_Post import *
from APIs.Get_Recent_Posts import *
from APIs.Add_Comment import *
from APIs.Upvote_downvote import *
from APIs.Get_comments_of_a_post import *
from flask_restful import Api

from app import app

api = Api(app)


api.add_resource(Create_profile,'/beyond-the-seas.org/api/create_profile')
api.add_resource(Get_all_post,'/beyond-the-seas.org/api/newsfeed/get_posts')
api.add_resource(Get_Comment_of_a_post,'/beyond-the-seas.org/api/newsfeed/<post_id>/get_comments')
api.add_resource(Add_post,'/beyond-the-seas.org/api/newsfeed/add_post')
api.add_resource(Add_comment,'/beyond-the-seas.org/api/newsfeed/add_comment')
api.add_resource(Upvote_or_Downvote_for_post,'/beyond-the-seas.org/api/newsfeed/post/<vote>')
api.add_resource(Upvote_or_Downvote_for_comment,'/beyond-the-seas.org/api/newsfeed/comment/<vote>')

