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
    altitude    = db.Column(db.Integer)
    desc        = db.Column(db.String)
    plants      = db.relationship("Flora",
                    secondary="plant_locations",
                    back_populates="locations")

    def __repr__(self):
        return "<Location: {}>".format(self.name)