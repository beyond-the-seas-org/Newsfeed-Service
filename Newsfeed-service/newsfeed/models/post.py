from newsfeed import db

class PostModel(db.Model):

    """
    primary key: id
    other fields: post_desc,date(store both date and time), Profile_id, community_id(can be null.if the post is from only profile,not from a community), type(newsfeed or community),upvotes,downvotes
    """

    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    post_desc = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.DateTime)
    profile_id = db.Column(db.Integer, nullable=False)
    community_id = db.Column(db.Integer,db.ForeignKey("community.id"),nullable=True)
    type = db.Column(db.String(15))
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    post_image = db.Column(db.String(255),nullable=True)


    #if a post is deleted than all its comments, upvote and downvote entries also should be deleted

    comment_child = db.relationship('CommentModel', backref='postmodel', cascade='all, delete')
    upvote_child = db.relationship('UpvoteModel', backref='postmodel', cascade='all, delete')
    upvote_child = db.relationship('DownvoteModel', backref='postmodel', cascade='all, delete')  

    # create a json method
    def json(self):
        return {
            'id': self.id,
            'post': self.post_desc,
            'date': self.date,
            'profile_id': self.profile_id,
            'community_id': self.community_id,
            'type':self.type,
            'upvotes':self.upvotes,
            'downvotes':self.downvotes
        }