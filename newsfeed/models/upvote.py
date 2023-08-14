from newsfeed import db

class UpvoteModel(db.Model):

    """
    primary key: id
    other fields: post_id,comment_id,type(comment or post),profile_id
    """

    __tablename__ = 'upvote'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    post_id = db.Column(db.Integer,db.ForeignKey("post.id"), nullable=True)
    comment_id = db.Column(db.Integer,db.ForeignKey("comment.id"),nullable=True)
    type = db.Column(db.String(15),nullable = False)
    profile_id = db.Column(db.Integer,nullable=False)
     

    # create a json method
    def json(self):
        return {
            'id': self.id,
            'post_id': self.post_id,
            'comment_id':self.comment_id,
            'profile_id': self.profile_id,
            'type':self.type,
           
        }