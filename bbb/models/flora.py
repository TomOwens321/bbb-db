from bbb import db
from sqlalchemy.ext.hybrid import hybrid_property

class Flora(db.Model):
    """
    Plants and such
    """
    __tablename__ = 'flora'
    id          = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String)
    desc        = db.Column(db.String)
    sub_species = db.Column(db.String)
    variety     = db.Column(db.String)
    genus_id    = db.Column(db.Integer, db.ForeignKey('genus.id'))
    genus       = db.relationship("Genus")
    species_id  = db.Column(db.Integer, db.ForeignKey('species.id'))
    species     = db.relationship("Species")
    germination_code = db.Column(db.String)

    @hybrid_property
    def name(self):
        name = "{} {}".format(self.genus.name,self.species.name)
        if self.sub_species:
            name += " ssp: {}".format(self.sub_species)
        if self.variety:
            name += " var: {}".format(self.variety)
        return name

    def __repr__(self):
        return "<Plant:{} {}>".format(self.genus.name,self.species.name)