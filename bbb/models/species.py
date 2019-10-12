from bbb import db
from .flora import Flora
from .fauna import Fauna

class Species(db.Model):
    __tablename__ = 'species'
    id     = db.Column(db.Integer, primary_key=True)
    name   = db.Column(db.String, unique=True)
    desc   = db.Column(db.String)
    plants = db.relationship("Flora")
    bugs   = db.relationship("Fauna")

    def __repr__(self):
        return "<Species:{}>".format(self.name)