from newsfeed.apis.Add_Post import *
from newsfeed.apis.Get_Recent_Posts import *
from newsfeed.apis.Add_Comment import *
from newsfeed.apis.Upvote_downvote import *
from newsfeed.apis.Get_comments_of_a_post import *
from newsfeed.apis.Edit_post import *
from newsfeed.apis.Delete_post import *
from newsfeed.apis.Get_own_posts import *
from newsfeed.apis.Edit_comment import *
from newsfeed.apis.search_post import *

Newsfeed = api.namespace('api/newsfeed')

Newsfeed.add_resource(Get_all_post,'/<current_user_id>/get_posts') 
Newsfeed.add_resource(Get_Comment_of_a_post,'/<current_user_id>/<post_id>/get_comments')
Newsfeed.add_resource(Add_post,'/add_post')
Newsfeed.add_resource(Add_comment,'/add_comment')
Newsfeed.add_resource(Upvote_or_Downvote_for_post,'/post/<vote>/<i_or_d>') # "i_or_d" means increament or decrement
Newsfeed.add_resource(Upvote_or_Downvote_for_comment,'/comment/<vote>/<i_or_d>')  #"i_or_d" means increament or decrement
Newsfeed.add_resource(Edit_post,'/edit_post')
Newsfeed.add_resource(Edit_comment,'/edit_comment')
Newsfeed.add_resource(Delete_post,'/delete_post')
Newsfeed.add_resource(Get_own_posts,'/<user_id>/get_own_posts') #this API req will come from "user service"
Newsfeed.add_resource(Search_Post,'/<curren_user_id>/search') #this API req will come from "user service"


