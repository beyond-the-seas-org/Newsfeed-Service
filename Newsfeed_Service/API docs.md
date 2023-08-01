##Profile
### create_profile (post method)

post request from frontend ==>

{
"username":"XYZ",
"first_name":"ABC",
"last_name":"PQR",
"primary_email":"anik2023@gmail.com",
"gender":"male",
"age":25,
"secondary_email":"XYZA2023@gmail.com",
"bsc_year_of_passing":2018,
"ms_year_of_passing":2020,
"bsc_cgpa":3.70,
"ms_cgpa":3.90,
"bsc_university":"Bangladesh University of Engineering and Technology",
"ms_university":"Bangladesh University of Engineering and Technology",
"github_link":"https://github.com/beyond-the-seas3-org",
"linkedin_link":"linkdin3",
"current_address":"Dhaka,Bangladesh",
"website_link":"website3",
"gre_verbal_quant_score":10,
"gre_awa_score":10.0,
"toefl_score":10 ,
"ielts_score":7.5
}


## Newsfeed


### /getposts(Get method)

response from backend==>
[
    {
        "comments": [
            {
                "comment": "this is test comment 2",
                "commentor": "asif"
            }
        ],
        "downvotes": 0,
        "post_desc": "This is a test post 1",
        "post_id": 1,
        "upvote": 0,
        "user_id": 1,
        "user_name": "XYZ"
    },
    {
        "comments": [
            {
                "comment": "this is test comment 3",
                "commentor": "anik"
            }
        ],
        "downvotes": 0,
        "post_desc": "This is a test post 2",
        "post_id": 2,
        "upvote": 0,
        "user_id": 2,
        "user_name": "asif"
    },
    {
        "comments": [
            {
                "comment": "this is test comment 1",
                "commentor": "XYZ"
            },
            {
                "comment": "this is test comment 4",
                "commentor": "asif"
            }
        ],
        "downvotes": 0,
        "post_desc": "This is a test post 3",
        "post_id": 3,
        "upvote": 0,
        "user_id": 3,
        "user_name": "anik"
    }
]


### /addpost(Post method)

post request from frontend ==>
{
 "user_id" : 2,
 "post_desc": "This is a test post4",
 "date":"2023-07-26 11:30:00",
 "type":"newsfeed"
}


### /addcomment(Post method)

post request from frontend ==>

{
 "user_id": 1,
 "post_id": 3,
 "date":"2023-07-31 18:30:00",
 "comment": "this is test comment 1"
}


### /post/<vote> (upvote or downvote) (post method)

post request from frontend ==>

{
 "post_id":1
}


### /comment/<vote> (upvote or downvote) (comment method)

post request from frontend ==>

{
 "comment_id":1
}












