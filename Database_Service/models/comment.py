from app import db

class CommentModel(db.Model):

    """
    primary key: id
    other fields: comment,date(store both date and time), Profile_id,post_id,upvotes,downvotes
    """

    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.DateTime)
    profile_id = db.Column(db.Integer,db.ForeignKey("student.id"), nullable=False)
    post_id = db.Column(db.Integer,db.ForeignKey("post.id"),nullable=False)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)

    

    # create a json method
    def json(self):
        return {
            'id': self.id,
            'comment': self.comment,
            'date': self.date,
            'profile_id': self.profile_id,
            'post_id': self.post_id,
            'upvotes':self.upvotes,
            'downvotes':self.downvotes
        }