from bbb import db
from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref, sessionmaker

class PlantBugs(db.Model):

    __tablename__ = 'plant_bugs'
    flora_id = db.Column(db.Integer, db.ForeignKey('flora.id'), primary_key=True)
    fauna_id = db.Column(db.Integer, db.ForeignKey('fauna.id'), primary_key=True)
