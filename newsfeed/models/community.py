from newsfeed import db

class CommunityModel(db.Model):

    """
    primary key: id
    other fields: name,desc
    """

    __tablename__ = 'community'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    desc = db.Column(db.String(100))

    #if a commujnity is deleted than all its posts also should be deleted

    post_child = db.relationship('PostModel', backref='communitymodel', cascade='all, delete')
    

    # create a json method
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'desc':self.desc
            
        }