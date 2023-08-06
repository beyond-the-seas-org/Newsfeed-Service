from newsfeed.apis.Add_Post import *
from newsfeed.apis.Get_Recent_Posts import *
from newsfeed.apis.Add_Comment import *
from newsfeed.apis.Upvote_downvote import *
from newsfeed.apis.Get_comments_of_a_post import *
from newsfeed.apis.Edit_post import *
from newsfeed.apis.Delete_post import *
from newsfeed.apis.Get_own_posts import *
from newsfeed.apis.Edit_comment import *

api.add_resource(Get_all_post,'/beyond-the-seas.org/api/newsfeed/get_posts') 
api.add_resource(Get_Comment_of_a_post,'/beyond-the-seas.org/api/newsfeed/<post_id>/get_comments')
api.add_resource(Add_post,'/beyond-the-seas.org/api/newsfeed/add_post')
api.add_resource(Add_comment,'/beyond-the-seas.org/api/newsfeed/add_comment')
api.add_resource(Upvote_or_Downvote_for_post,'/beyond-the-seas.org/api/newsfeed/post/<vote>')
api.add_resource(Upvote_or_Downvote_for_comment,'/beyond-the-seas.org/api/newsfeed/comment/<vote>')
api.add_resource(Edit_post,'/beyond-the-seas.org/api/newsfeed/edit_post')
api.add_resource(Edit_comment,'/beyond-the-seas.org/api/newsfeed/edit_comment')
api.add_resource(Delete_post,'/beyond-the-seas.org/api/newsfeed/delete_post')
api.add_resource(Get_own_posts,'/beyond-the-seas.org/api/newsfeed/<user_id>/get_own_posts') #this API req will come from "user service"



