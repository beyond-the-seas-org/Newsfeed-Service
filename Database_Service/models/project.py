from app import db

class ProjectModel(db.Model):
    """
    primary key: id
    other fields: name, description, link
    """

    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False, unique=True)
    description = db.Column(db.String(5000), nullable=False)
    link = db.Column(db.String(500))

    # create a json method
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'link': self.link
        }
