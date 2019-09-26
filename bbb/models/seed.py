from bbb import db

class Seed(db.Model):
    """
    Table for seed collection data
    """
    __tablename__ = 'seed'
    id = db.Column(db.Integer, primary_key=True)
    flora_id = db.Column(db.Integer, db.ForeignKey('flora.id'))
    flora    = db.relationship("Flora")
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    location    = db.relationship("Location")
    quantity    = db.Column(db.Float)
    uom         = db.Column(db.String)
    collection_lot  = db.Column(db.String)
    analysis_lot    = db.Column(db.String)

    def __repr__(self):
        return "<Seed: {}>".format(self.collection_lot)