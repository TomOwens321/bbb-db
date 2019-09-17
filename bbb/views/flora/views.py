from flask import render_template, flash, request
from bbb.models import Flora, Genus, Species
from bbb import db
from . import flora

@flora.route('/flora')
def list_flora():
    all_flora = db.session.query(Flora).all()
    return render_template("flora/flora.html", items=all_flora)