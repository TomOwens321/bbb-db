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
    family_id   = db.Column(db.Integer, db.ForeignKey('family.id'))
    family      = db.relationship("Family")
    genus_id    = db.Column(db.Integer, db.ForeignKey('genus.id'))
    genus       = db.relationship("Genus")
    species_id  = db.Column(db.Integer, db.ForeignKey('species.id'))
    species     = db.relationship("Species")
    germination_code = db.Column(db.String)
    bugs        = db.relationship("Fauna",
                   secondary="plant_bugs",
                   back_populates="plants")
    locations   = db.relationship("Location",
                   secondary="plant_locations",
                   back_populates="plants")

    @hybrid_property
    def name(self):
        if self.genus and self.species:
            name = "{} {}".format(self.genus.name,self.species.name)
            if self.sub_species:
                name += " ssp: {}".format(self.sub_species)
            if self.variety:
                name += " var: {}".format(self.variety)
            return name
        else:
            return None

    @hybrid_property
    def genus_name(self):
        if self.genus:
            return self.genus.name
        else:
            return None
    @hybrid_property
    def species_name(self):
        if self.species:
            return self.species.name
        else:
            return None

    @hybrid_property
    def family_name(self):
        if self.family:
            return self.family.name
        else:
            return None

    def __repr__(self):
        if self.genus:
            return "<Plant:{} {}>".format(self.genus.name,self.species.name)
        else:
            return "Plant: None>"