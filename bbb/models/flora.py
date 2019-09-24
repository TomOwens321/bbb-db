from bbb import db
from sqlalchemy.ext.hybrid import hybrid_property
from .relations import PlantBugs

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
    bugs       = db.relationship("Fauna",
                   secondary="plant_bugs",
                   back_populates="plants")

    @hybrid_property
    def name(self):
        name = "{} {}".format(self.genus.name,self.species.name)
        if self.sub_species:
            name += " ssp: {}".format(self.sub_species)
        if self.variety:
            name += " var: {}".format(self.variety)
        return name

    @hybrid_property
    def genus_name(self):
        if self.genus.name:
            return self.genus.name
        else:
            return None
    @hybrid_property
    def species_name(self):
        if self.species.name:
            return self.species.name
        else:
            return None

    @hybrid_property
    def family_name(self):
        if self.family.name:
            return self.family.name
        else:
            return None

    def __repr__(self):
        return "<Plant:{} {}>".format(self.genus.name,self.species.name)