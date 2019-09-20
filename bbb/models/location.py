from bbb import db

class Location(db.Model):
    """
    Locations
    """
    __tablename__ = 'location'
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String)
    city        = db.Column(db.String)
    state       = db.Column(db.String)
    lattitude   = db.Column(db.Float)
    longitude   = db.Column(db.Float)
    desc        = db.Column(db.String)

    def __repr__(self):
        return "<Location: {}>".format(self.name)