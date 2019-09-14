from bbb import db

class Fauna(db.Model):
    """
    Plants and such
    """
    __tablename__ = 'fauna'
    id          = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String)
    desc        = db.Column(db.String)
    genus_id    = db.Column(db.Integer, db.ForeignKey('genus.id'))
    genus       = db.relationship("Genus")
    species_id  = db.Column(db.Integer, db.ForeignKey('species.id'))
    species     = db.relationship("Species")

    def __repr__(self):
        return "<Bug:{} {}>".format(self.genus.name,self.species.name)