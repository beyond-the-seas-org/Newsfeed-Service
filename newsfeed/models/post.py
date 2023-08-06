from newsfeed import db

class PostModel(db.Model):

    """
    primary key: id
    other fields: post_desc,date(store both date and time), Profile_id, community_id(can be null.if the post is from only profile,not from a community), type(newsfeed or community),upvotes,downvotes
    """

    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    post_desc = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.DateTime)
    profile_id = db.Column(db.Integer,db.ForeignKey("student.id"), nullable=False)
    community_id = db.Column(db.Integer,db.ForeignKey("community.id"),nullable=True)
    type = db.Column(db.String(15))
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)

    

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