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


    # create a json method
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'desc':self.desc
            
        }