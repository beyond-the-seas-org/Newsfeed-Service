from app import db 

student_project = db.Table("student_project",
    db.Column("student_id", db.ForeignKey("student.id"), primary_key=True),
    db.Column("project_id", db.ForeignKey("project.id"), primary_key=True)
)

student_field = db.Table("student_field",
    db.Column("student_id", db.ForeignKey("student.id"), primary_key=True),
    db.Column("field_id", db.ForeignKey("field.id"), primary_key=True)
)

student_publication = db.Table("student_publication",
    db.Column("student_id", db.ForeignKey("student.id"), primary_key=True),
    db.Column("publication_id", db.ForeignKey("publication.id"), primary_key=True)
)