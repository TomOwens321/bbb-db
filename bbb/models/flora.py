from bbb import db

class Flora(db.Model):
    """
    Plants and such
    """
    __tablename__ = 'flora'
    id          = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String)
    desc        = db.Column(db.String)
    genus_id    = db.Column(db.Integer, db.ForeignKey('genus.id'))
    genus       = db.relationship("Genus")
    species_id  = db.Column(db.Integer, db.ForeignKey('species.id'))
    species     = db.relationship("Species")
    germination_code = db.Column(db.String)

    def __repr__(self):
        return "<Plant:{} {}>".format(self.genus.name,self.species.name)